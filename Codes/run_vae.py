#! /usr/bin/env python
"""
A quick exemple of running the sentence-VAE model on the dataset loaded 
directly from torchtext's new API.

Usage:
------

`python run_vae.py --data wikitext-2 --epochs 1 --savedir dumps/`

Check the detail of how to use this script with:
    
    ```
    python run_vae.py --help
    ```
"""

import torchtext as tt
import torch as t
import numpy as np
import pandas as pd
from collections import Counter
from tqdm import tqdm
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from model import SentenceVAE


def create_vocab(dataset, verbose=True):
    """
    Create the vocabulary based on a RawText Dataset instance.
    
    Note
    ----
    This functions also returns the collate_batch function which depends on the 
    vocab object being created as well as the negative log-likelihood function
    (the latter need the vocab object to know which index is the padding token).
    """
    counter = Counter()
    tokenizer = tt.data.get_tokenizer("basic_english")
    for line in tqdm(dataset, leave=False):
        counter.update(tokenizer(line))

    vocab = tt.legacy.vocab.Vocab(counter, max_size=20000, min_freq=10, specials=('<sos>', '<eos>', '<unk>', '<pad>'))
    if verbose:
        print(f"""
    Vocabulary size: {len(vocab)}
    Index of padding token: {vocab['<pad>']}
    Index of unknown token: {vocab['<unk>']}
    Index of sos token: {vocab['<sos>']}
    Index of eos token: {vocab['<eos>']}
            """)

    # function to map text to ids (integers)
    text_transform = lambda x:  [vocab['<sos>']] + [vocab[token] for token in tokenizer(x)] + [vocab['<eos>']]
    def collate_batch(batch, pad_val=vocab['<pad>']):
        "This function will be used to actually create the torch tensor batch from the text data (which is given line by line from the iterator)"
        target_list, input_list, lengths = [], [], []
        for _text in batch:
            processed_text = t.tensor(text_transform(_text))
            input_list.append(processed_text[:-1])
            target_list.append(processed_text[1:])
            lengths.append(len(processed_text)-1)
        return pad_sequence(input_list, padding_value=float(pad_val), batch_first=True), \
                pad_sequence(target_list, padding_value=float(pad_val), batch_first=True), t.tensor(lengths)
    
    # Creating the NLL function:
    NLL = t.nn.NLLLoss(ignore_index=vocab.stoi['<pad>'], reduction='sum')
    
    return vocab, collate_batch, NLL

def read_parameters_config(vocab, config_file=None):
        if config_file is None:
            param = {
            'vocab_size': len(vocab),
            'embedding_size': 353,
            'rnn_type': 'gru',
            'hidden_size': 128,
            'word_dropout': 0.62,
            'embedding_dropout': 0,
            'latent_size': 13,
            'sos_idx': vocab.stoi['<sos>'],
            'eos_idx': vocab.stoi['<eos>'],
            'pad_idx': vocab.stoi['<pad>'],
            'unk_idx': vocab.unk_index,
            'max_sequence_length': 25,
            'num_layers' : 1,
            'bidirectional': False,
            }
        else:
            import json
            # Load from file
            with open(config_file, 'r') as f:
                param = json.load(f)
            # Add vocab related parameters
            param = param | {'vocab_size': len(vocab),
                             'sos_idx': vocab.stoi['<sos>'],
                            'eos_idx': vocab.stoi['<eos>'],
                            'pad_idx': vocab.stoi['<pad>'],
                            'unk_idx': vocab.unk_index,}
        return param

def kl_anneal_function(anneal_function, step, k, x0):
    # this function could be made periodic (modulo) over epochs too...
    # there are a lot of possiblities to try
    if anneal_function == 'logistic':
        return np.asarray(1/(1+np.exp(-k*(step-x0))))
    elif anneal_function == 'linear':
        return np.minimum(1, step/x0)
    
def loss_fn(logp, target, length, mean, logv, anneal_function, step, k, x0, NLL_func):

    # cut-off unnecessary padding from target, and flatten
    target = target[:, :t.max(length).item()].contiguous().view(-1)
    logp = logp.view(-1, logp.size(2))

    # Negative Log Likelihood
    NLL_loss = NLL_func(logp, target)

    # KL Divergence
    KL_loss = -0.5 * t.sum(1 + logv - mean.pow(2) - logv.exp())
    KL_weight = kl_anneal_function(anneal_function, step, k, x0)

    return NLL_loss, KL_loss, KL_weight

def train_one_epoch(loader, model, optim, batch_size, nll_func, device='cuda'):
    model.train()
    total_loss = 0.
    all_losses = {'KL':[], 'nll':[], 'total':[]}
    # iterate over the data:
    for step, (input_batch, target_batch, lengths_batch) in tqdm(enumerate(loader), total=len(loader), leave=False, miniters=100, desc='Training'):
        # Forward pass through the model
        logp, mean, logv, z = model(input_batch.to(device), lengths_batch)

        # compute the loss
        nllloss, kl, weight = loss_fn(logp, target_batch.to(device), lengths_batch, mean, logv, 'logistic', step, 0.0025, 2500, nll_func)
        loss = (nllloss + t.tensor(weight) * kl)/batch_size

        # propagate error and update model parameters
        optim.zero_grad() # zero out the previous gradients stored
        loss.backward() # compute the new gradient by backprop the loss
        optim.step() # update each parameter w.r.t their gradient

        # keep track of the loss (for plotting later for instance)
        total_loss += loss.item()
        all_losses['nll'].append(nllloss.item()/batch_size)
        all_losses['KL'].append(kl.item()/batch_size)
        all_losses['total'].append(loss.item())
    total_loss /= step+1
    
    return total_loss, all_losses

def evaluate_model(loader, model, batch_size, nll_func, device='cuda'):
    model.eval()
    val_loss = 0.
    # iterate over the data:
    for step, (input_batch, target_batch, lengths_batch) in tqdm(enumerate(loader), leave=False, total=len(loader), miniters=100, desc='Evaluating model'):
        logp, mean, logv, z = model(input_batch.to('cuda'), lengths_batch)
        # compute the loss
        nllloss, kl, weight = loss_fn(logp, target_batch.to(device), lengths_batch, mean, logv, 'logistic', 10, 0.0025, 1500, nll_func)
        loss = (nllloss + t.tensor(weight) * kl)/batch_size
        val_loss += loss.item()
    val_loss /= step+1
    return val_loss

def bookkeep_losses(data_loss, new_epoch_losses):
    "Updating a pandas dataframe containing losses of all iterations during training"
    return data_loss.append(pd.DataFrame(new_epoch_losses), ignore_index=True)

if __name__ == '__main__':
    import argparse
    import os
    import time
    
    # Read in command line arguments 
    p = argparse.ArgumentParser(description='Train the sentence VAE model on some dataset.')
    p.add_argument("--epochs", type=int, default=1, help="Number of epochs to train (one epoch = an entire dataset sweep)")
    p.add_argument("--config", type=str, help="Path of config file if any (if none will use some default values, see code).")
    p.add_argument("--batch", type=int, default=32, help="Batch size")
    p.add_argument("--data", type=str, choices=['wikitext-2', 'wikitext-103', 'ptb'], default='wikitext-103', help="Name of the dataset to train on.")
    p.add_argument("--rootdir", type=str, default='./data', help="Root directory of folder containing dataset(s). If a dataset is not present it will be downloaded in this directory.")
    p.add_argument("--savedir", type=str, default='./dumps', help="Directory where model checkpoints are saved.")
    args = p.parse_args()
    n_epochs = args.epochs
    batch_size = args.batch
    rootdir = args.rootdir
    
    # Create time-stamp and a directory for the current run:
    timestamp = time.strftime('%Y-%b-%d-%H:%M:%S', time.gmtime()) # this is simply a string with current date and time
    savedir = os.path.join(args.savedir, timestamp)
    os.makedirs(savedir) # we create a directory inside the savedir directory with the timestamp for its name
    
    # Print information:
    print(f"""
    Number of epochs: {n_epochs}
    Batch size: {batch_size}
    Dataset used: {args.data}
    Data will be (down)loaded from/to {rootdir}
    Model will be saved in {savedir}
    VAE model configuration file: {args.config}
          """)
    # tokenizer (can use any other, e.g. a dutch specific one)
    tokenizer = tt.data.get_tokenizer("basic_english")

    # Handle on one of the torchtext dataset class
    if args.data == 'wikitext-2':
        DataSet = tt.datasets.WikiText2
    elif args.data == 'wikitext-103':
        DataSet = tt.datasets.WikiText103
    elif args.data == 'ptb':
        DataSet = tt.datasets.PennTreebank
    else:
        raise ValueError("Dataset must be one of [wikitext-2, wikitext-103, ptb].")
    
    # Create vocabulary:    
    # Load from existing directory to avoid downloading again
    print("Parsing training split of the dataset to create vocabulary list...")
    train = DataSet(root=rootdir, split=('train'))
    vocab, collate_fn, NLL = create_vocab(train) # this output the vocab object, 
                                                 # the collate_fn for dataloader 
                                                 # later, and a NLL function for the loss_fn
                                                 # (look inside the code of 'create_vocab'
                                                 # for more info)
    
    # The VAE model, with len(vocab):
    param = read_parameters_config(vocab, config_file=args.config)
    model = SentenceVAE(**param)
    mdoel = model.to('cuda')

    optimizer = t.optim.Adam(params=model.parameters(), lr=0.001)
    df_loss = pd.DataFrame({'KL':[], 'nll':[], 'total':[]})
    for epoch in range(n_epochs):
        print("")
        # Get a data loader iterator
        train, val = DataSet(root=rootdir, split=('train', 'valid'))
        train_dataloader = DataLoader(list(train), batch_size=batch_size, shuffle=True,
                                      collate_fn=collate_fn) # here we use the collate_fn created earlier
        
        # Training is wrapped in one function to keep code tidy
        total_loss, losses = train_one_epoch(train_dataloader, model, optimizer, batch_size, NLL) # here we use the NLL function created earlier
        df_loss = bookkeep_losses(df_loss, losses)
        
        # Validation set (also wrapped in a function)
        val_dataloader = DataLoader(list(val), batch_size=batch_size, shuffle=True,
                                      collate_fn=collate_fn)
        val_loss = evaluate_model(val_dataloader, model, batch_size, NLL)
        
        print(f"Epoch: {epoch+ 1}/{n_epochs} | TRAIN LOSS = {total_loss:.3f} | VAL LOSS = {val_loss:.3f}")
        
        # Save model after each epoch
        checkpoint_path = os.path.join(savedir, f"Epoch_{epoch+1}.pytorch") # file path
        t.save(model.state_dict(), checkpoint_path)
    
    # Save losses, and plot if "--plot" was used in the command line arguments
    df_loss.to_csv(os.path.join(savedir, 'losses.csv'))
        
