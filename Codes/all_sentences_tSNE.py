#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:25:13 2022

@author: navjab
"""
import numpy as np
from glob import glob
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns
filenames=glob("*ptb.npy")
# all_sent=[]
# for file in filenames:
#     with open (file,'r') as f:
#         a=f.readlines()
#         all_sent.append(a)
# with open ('all_sent.txt','w') as b:        
#     for sets in all_sent:  
#         for sent in sets:
#             b.write(sent)
mydict={}
for n in filenames:  
    data=np.load(n)  
  
    
    data_emb = TSNE(n_components=2, learning_rate=100,init='pca').fit_transform(data)    
    mydict["%s" %n] =data_emb
# file='TSNE.npy'
# data=np.load(file, allow_pickle=True)
keys=[]
values=[]
keyList=[]
styles=[]
for key, value in mydict.items():
    for i in value:
        values.append(i)
        keys.append(key)
        
 ### tracking      
for i in range(len(keys)):
    
    if i<400:
        if (i%2==1):
            keys[i]=2
            keyList.append('past')
            styles.append('FP_Pair') 
        if (i%2==0):
            keys[i]=1
            keyList.append('future')
            styles.append('FP_Pair')  
    if i<800 and i>=400:
        if (i%2==1):
           keys[i]=4
           keyList.append('passive')
           styles.append('AP_Pair') 
        if (i%2==0):
           keys[i]=3
           keyList.append('active')
           styles.append('AP_Pair') 
    if i<1200 and i>=800:
       if (i%2==1):
           keys[i]=6
           keyList.append('negative')
           styles.append('PN_Pair') 
       if (i%2==0):
           keys[i]=5
           keyList.append('positive')
           styles.append('PN_Pair') 
    if i<1600 and i>=1200:
       if (i%2==1):
           keys[i]=8
           keyList.append('plural')
           # styles.append('SP_Pair') 
       if (i%2==0):
           keys[i]=7   
           keyList.append('singular')
           # styles.append('SP_Pair') 
values=np.array(values)
         
np.save('ALL.npy',values)    
sns.scatterplot(x=values[:,0], y=values[:,1],
              hue=keyList,#style=styles,
              data=values)
lgd=plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)  
  
plt.savefig('ALL', bbox_extra_artists=(lgd,), bbox_inches='tight')