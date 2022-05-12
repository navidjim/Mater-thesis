#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:41:45 2022

@author: navjab
"""

from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
from bayes_opt.util import load_logs
import torch as t
import torchtext as tt
import numpy as np
import pandas as pd
from model import SentenceVAE
from run_vae import create_vocab
from run_vae import train_one_epoch
from run_vae import evaluate_model
from torch.utils.data import DataLoader
from math import isnan
import numpy as np
from run_vae import bookkeep_losses


logger = JSONLogger(path="./ptb_optimization.json")
pbounds = {'hs': (6, 8), 'lrate': (-3, -2), 'wd': (0,0.8),'ed':(0,0.8), 'nl':(1, 2), 'ls':(10, 25)}
def trainVAE(hs, lrate, wd, ed, nl, ls):
    
        import argparse
        import os
        import time
        # Read in command line arguments 
        p = argparse.ArgumentParser(description='Train the sentence VAE model on some dataset.')
        p.add_argument("--epochs", type=int, default=20, help="Number of epochs to train (one epoch = an entire dataset sweep)")
        p.add_argument("--config", type=str, help="Path of config file if any (if none will use some default values, see code).")
        p.add_argument("--batch", type=int, default=128, help="Batch size")
        p.add_argument("--data", type=str, choices=['wikitext-2', 'wikitext-103', 'ptb'], default='ptb', help="Name of the dataset to train on.")
        p.add_argument("--rootdir", type=str, default='./data', help="Root directory of folder containing dataset(s). If a dataset is not present it will be downloaded in this directory.")
        p.add_argument("--savedir", type=str, default='./dumps', help="Directory where model checkpoints are saved.")
        args = p.parse_args()
        epochs = args.epochs
        batch_size = args.batch
        rootdir = args.rootdir
       
        if args.data == 'wikitext-2':
            DataSet = tt.datasets.WikiText2
        elif args.data == 'wikitext-103':
            DataSet = tt.datasets.WikiText103
        elif args.data == 'ptb':
            DataSet = tt.datasets.PennTreebank
        else:
            raise ValueError("Dataset must be one of [wikitext-2, wikitext-103, ptb].")
        train = DataSet(root=rootdir, split=('train'))
        vocab, collate_fn, NLL = create_vocab(train)
        param = {
                'vocab_size': len(vocab),
                'embedding_size': 350,
                'rnn_type': 'gru',
                'hidden_size': 2**int(hs),
                'word_dropout': wd,
                'embedding_dropout': ed,
                'latent_size': int(ls),
                'sos_idx': vocab.stoi['<sos>'],
                'eos_idx': vocab.stoi['<eos>'],
                'pad_idx': vocab.stoi['<pad>'],
                'unk_idx': vocab.unk_index,
                'max_sequence_length': 30,
                'num_layers' : int(nl),
                'bidirectional': False,
                }
        model = SentenceVAE(**param)
        model = model.to('cuda')
        optim = t.optim.Adam(params=model.parameters(), lr=10**lrate)
        ELBOlist=[]
        # df_loss = pd.DataFrame({'KL':[], 'nll':[], 'total':[]})
        for epoch in range(epochs):
                print("")
                # Get a data loader iterator
                train, val = DataSet(root=rootdir, split=('train', 'valid'))
                train_dataloader = DataLoader(list(train), batch_size=batch_size, shuffle=True,
                                              collate_fn=collate_fn) # here we use the collate_fn created earlier
                
                # Training is wrapped in one function to keep code tidy
                total_loss, losses = train_one_epoch(train_dataloader, model, optim, batch_size, NLL) # here we use the NLL function created earlier
                # df_loss = bookkeep_losses(df_loss, losses)
               
                val_dataloader = DataLoader(list(val), batch_size=batch_size, shuffle=True,
                                      collate_fn=collate_fn)
                val_loss = evaluate_model(val_dataloader, model, batch_size, NLL)
             
                ELBOlist.append(val_loss)
                
            
       
        if np.isnan(-np.mean(ELBOlist[-5:]))== True:
           return 0
        else : 
           return -np.mean(ELBOlist[-5:]) 
    # print("ELBO=",ELBOlist) , print("df",df_loss) 
    # trainVAE(256,-3, , ed, nl, ls)
     # -np.mean(ELBOlist)  
optimizer = BayesianOptimization(
    f=trainVAE,
    pbounds=pbounds,
    random_state=1,
)
optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)
load_logs(optimizer, logs=["/home/lacnsg/navjab/Desktop/Sentence-VAE-master/ptblogs.json"])
optimizer.maximize(
    init_points=2,
    n_iter=200,
)

print(optimizer.max)
