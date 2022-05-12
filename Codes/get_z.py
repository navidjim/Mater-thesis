#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:34:02 2022

@author: navjab
"""

import torch as t
import json
from model import SentenceVAE
from collections import Counter
from tqdm.notebook import tqdm
import torchtext as tt
from torch.utils.data import DataLoader 
from run_vae import create_vocab
import numpy as np
from glob import glob
train = tt.datasets.PennTreebank(root='/home/lacnsg/navjab/Desktop/Sentence-VAE-master/data/' , split=('train'))
vocab, collate_fn, NLL = create_vocab(train)
config_file = '/home/lacnsg/navjab/Desktop/Sentence-VAE-master/dumps/ptb3/configs.json'
model_file = '/home/lacnsg/navjab/Desktop/Sentence-VAE-master/dumps/ptb3/Epoch_60.pytorch'
#### load the parameters
with open(config_file, 'r') as f:
    param = json.load(f)
# Add vocab-dependent variables to param:
param.update( {'vocab_size': len(vocab),
                              'sos_idx': vocab.stoi['<sos>'],
                            'eos_idx': vocab.stoi['<eos>'],
                            'pad_idx': vocab.stoi['<pad>'],
                            'unk_idx': vocab.unk_index})

print("Parameters are:")
print(param)
model = SentenceVAE(**param)
# Load the state of the weight and biases of the neural nets
model.load_state_dict(t.load(model_file))
print("Model loaded from %s" % model_file)
model = model.to('cuda')
filenames=glob('*.txt')
for file in filenames:
    with open(file) as f:
        raw = f.read()
        lines = raw.split('\n')
    z_sentences = []
    for sent in lines[:-1]:
        input_tensor, _, length = collate_fn([sent])
        _, _, _, z = model(input_tensor.to('cuda'), length.to('cuda'))
        z_sentences.append(z.cpu().detach().numpy().squeeze())
    
    z_sentences = np.asarray(z_sentences)
    np.save(file.replace('.txt', ''),z_sentences)
