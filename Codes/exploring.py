#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:31:50 2022

@author: navjab
"""
import numpy as np
import pandas as pd
import seaborn as sns
import scipy
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp , ttest_rel
from glob import glob
import json
import statsmodels
from statsmodels.stats.multitest import multipletests

files=glob('*.npy')
# zfiles=glob('*ptb.npy')
# for file, zf in zip(files,zfiles):
for file in files:
    f=np.load(file)
    type_1=f[::2]
    type_2=f[1::2]
    dif=[]
    for t1,t2 in zip(type_1,type_2):
        onesen=t2-t1
        dif.append(onesen)
        
    difference = np.asarray(dif)
   
    name=file.replace('.npy', '')
##############ttest

    t=ttest_1samp(difference, popmean=0)
    results = {}
    wilcox=[]
    for i in range(len(difference[1])):
       w=scipy.stats.wilcoxon(difference[:,i])
       wilcox.append(w)
    a= statsmodels.stats.multitest.multipletests(t[1],alpha=0.05, method='bonferroni')
    w=[]
    c=0
    for i in wilcox:
        w.append(i[1])
        c+=1
       
    p_val=t[1].tolist()
    cp_val=t[1].tolist()
    if w.index(sorted(w)[0])==w.index(sorted(w)[1]) and w.index(sorted(w)[0])==w.index(sorted(w)[2]):
        counter = 0
        elem_pos = []
        for i in w:
            if i == sorted(w)[1]:
                elem_pos.append(counter)
                counter = counter + 1
        wdim= [elem_pos]
    else :    
        wdim=[w.index(sorted(w)[0]),w.index(sorted(w)[1]),w.index(sorted(w)[2])]
    tdim=[cp_val.index(sorted(cp_val)[0]),cp_val.index(sorted(cp_val)[1]),cp_val.index(sorted(cp_val)[2])]
    keys = ['T_val' ,'p_val', 'MCT','correctedP','BONalpha','wilcoxon','wdim','tdim']
    values = [t[0].tolist(),p_val,a[0].tolist(),a[1].tolist(),a[3],wilcox[:],wdim,tdim]
    print(wdim,tdim)
    print("###############")
 
    for i in range(len(keys)):
        results[keys[i]] = values[i]    
    with open(f'{name}.ttest.json','w') as test:
        json.dump(results,test)
########### ploting
    sns.boxplot(data=difference)
    plt.savefig(f'{name}.png')
    plt.close()
    cat=[]
    for k in range(len(f)):
        if k%2==0:
            cat.append('type1')
        else:
            cat.append('type2')
    fig = plt.figure()

    ax = plt.subplot(111, projection='3d')
    ax.scatter(type_1[:,tdim[0]], type_1[:,tdim[1]], type_1[:,tdim[2]], label='type1')  
    ax.scatter(type_2[:,tdim[0]], type_2[:,tdim[1]], type_2[:,tdim[2]], label='type2')  
    plt.legend(loc="upper right")
 
    plt.savefig(f'{name}3d.png')
    plt.close()