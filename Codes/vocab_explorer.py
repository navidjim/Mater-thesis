#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:11:26 2022

@author: navjab
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
import csv

vocab_obj = t.load('vocab_wikitext103.pth')
mydict = dict(sorted(vocab_obj.stoi.items(), key=lambda item: item[1]))

with open('wikitext103_vocab.csv', 'w') as f:
    for key in mydict.keys():
        f.write("%s,%s\n"%(key,mydict[key]))
