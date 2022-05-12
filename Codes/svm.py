#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:31:01 2022

@author: navjab
"""

from glob import glob
import numpy as np
from sklearn import svm
import json
from sklearn.model_selection import KFold
import pandas as pd
filenames=glob('*.npy')


resultdic={}
for file in filenames:
    results=[]
    f=np.load(file)
    lables=np.asarray([k%2==1 for k in range (len(f))],dtype=int)   
    clf = svm.LinearSVC()
    k=int(len(f)/100)
    kf = KFold(n_splits=k)
    kf.get_n_splits(f)
    KFold(n_splits=k, random_state=None, shuffle=False)
    score=0
    for train_index, test_index in kf.split(f):
        X_train, X_test ,y_train,y_test = f[train_index], f[test_index],lables[train_index],lables[test_index]
        clf.fit(X_train,y_train)
        a=clf.score(X_test,y_test)
        score=score+a
    mean=score/k
    print(file ,"clf score is", mean)
    del clf
    resultdic.setdefault(file,mean)
df=pd.DataFrame.from_dict(resultdic, orient ='index') 
df.to_csv('svm_3_60.csv')  
# with open("svm.json", 'w') as f:

#     json.dump(results, f, indent=2)     
    
