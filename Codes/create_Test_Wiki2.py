# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:13:46 2022

@author: navid
"""


import numpy as np
#############################################  WIKITEXT2 ######################################################
# hfNOUN = ['game', 'computer', 'song', 'film','music','box'] # ommited music and added magazine since music wasnt countable
hfNOUN = ['game', 'computer', 'song', 'film','box','magazine','guitar']
hfnVERBS = ['leave', 'play', 'perform','watch','direct','use']
hfnPVEBS=['left','played','performed','watched','directed','used']
mfNOUN=['rubber','deer','puzzle','bishop','bullet','uncle','chair']
mfnVERBS=['cure','eat','receive','complete','accompany','strike']
mfnPVEBS=['cured','eaten','received','completed','accompanied','struck']
lfNOUN=['arrow','volcano','yeast','tea','oak','liver','mayer']
lfnVERBS=['put','laud','produce','drink','plant','change']
lfnPVEBS=['put','lauded','produced','drunk','planted','changed']
 #frequent future verbs 
futurefVERBS=['have','bring','replace','kill','help','use','see']
pastfVERBS=['had','brought','replaced','killed','helped','used','saw']
# frequent past verbs 
futurepVERBS=['begin','take','receive','call','find','play','give']
pastpVERBS=['began','took','received','called','found','played','gave']
nounlist=['game', 'computer', 'song', 'film','box','magazine']
sent_type_1 =[]
 
sent_type_2 =[] 
sent_type_3 =[] 


counter=0
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(hfNOUN) 
#     b=np.random.choice(hfnVERBS)
#     c=np.random.choice(hfNOUN)
#     if a==c:
#         continue
#     else:
#         positive = f"the {a} {b}s the {c}"
#         negative= f"the {a} does not {b} the {c}"
#     if negative  and positive in sent_type_1:
#         counter+=1
#         continue
#     else:
#         sent_type_1.append(positive)
#         sent_type_1.append(negative)
# with open ('hf_pnsentece_wiki2.txt', 'w') as lf:
#     for a in sent_type_1:
#         lf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1))   
####################################################   
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(mfNOUN) 
#     b=np.random.choice(mfnVERBS)
#     c=np.random.choice(mfNOUN)
#     if a==c:
#           continue
#     else:
#           positive = f"the {a} {b}s the {c}"
#           negative= f"the {a} does not {b} the {c}"
#     if negative  and positive in sent_type_1:     
#           counter+=1
#           continue
#     else:
#           sent_type_1.append(positive)
#           sent_type_1.append(negative)
# with open ('mf_pnsentece_wiki2.txt', 'w') as lf:
#     for a in sent_type_1:
#         lf.write("%s \n" %a)
#         print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
####################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(lfNOUN) 
#     b=np.random.choice(lfnVERBS)
#     c=np.random.choice(lfNOUN)
#     if a==c:
#         continue
#     else:
#         positive = f"the {a} {b}s the {c}"
#         negative= f"the {a} does not {b} the {c}"
#     if positive and negative in sent_type_1:
#         counter+=1
#         continue
#     else:
#         sent_type_1.append(positive)
#         sent_type_1.append(negative)
# with open ('lf_npsentece_wiki2.txt', 'w') as lf:
#     for a in sent_type_1:
#         lf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
##################################### ACTIVE PASSIVE ###########
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(hfNOUN) 
#     b=np.random.choice(hfnVERBS)
#     c=np.random.choice(hfNOUN)
#     d=hfnPVEBS[hfnVERBS.index(b)]
#     if a==c:
#         continue
#     else:
#         active = f"the {a} {b}s the {c}"
#         passive= f"the {c} is {d} by the {a}"
#     if active  and passive in sent_type_1:
#         counter+=1
#         continue
#     else:
#         sent_type_1.append(active)
#         sent_type_1.append(passive)
# with open ('hfap_sentece_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
########################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(mfNOUN) 
#     b=np.random.choice(mfnVERBS)
#     c=np.random.choice(mfNOUN)
#     d=mfnPVEBS[mfnVERBS.index(b)]
#     if a==c:
#         continue
#     else:
#         active = f"the {a} {b}s the {c}"
#         passive= f"the {c} is {d} by the {a}"
#     if active  and passive in sent_type_1:
#           counter+=1
#           continue
#     else: 
#           sent_type_1.append(active)
#           sent_type_1.append(passive)
# with open ('mfap_sentece_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)  
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
#######################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(lfNOUN) 
#     b=np.random.choice(lfnVERBS)
#     c=np.random.choice(lfNOUN)
#     d=lfnPVEBS[lfnVERBS.index(b)]
#     if a==c:
#         continue
#     else:
#       active = f"the {a} {b}s the {c}"
#       passive= f"the {c} is {d} by the {a}"
#     if active  and passive in sent_type_1:
#         counter+=1
#         continue
#     else:
#       sent_type_1.append(active)
#       sent_type_1.append(passive)
# with open ('lfap_sentece_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)    
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
###########################################################
# while True :
#     if len(sent_type_1)==400:
#         break
#     a=np.random.choice(hfNOUN) 
#     b=np.random.choice(hfnVERBS)
#     c=np.random.choice(hfNOUN)
#     if a==c:
#         continue
#     else:
#         singular = f"the {a} is {b}ing the {c}"
#         plural= f"the {a}s are {b}ing the {c}s"
#     if singular  and plural in sent_type_1:
#         counter+=1
#         continue 
#     else:
#         sent_type_1.append(singular)
#         sent_type_1.append(plural)
# with open ('sphf_sentence_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a) 
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
###########################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(mfNOUN) 
#     b=np.random.choice(mfnVERBS)
#     c=np.random.choice(mfNOUN)
#     if a==c:
#         continue
#     else:
#       singular = f"the {a} is {b}ing the {c}"
#       if a=='baby':
#           a='babie'
#       if c== 'baby':
#           c= 'babie'
#       plural= f"the {a}s are {b}ing the {c}s"
#     if singular  and plural in sent_type_1:
#         counter+=1
#         continue
#     else:
#       sent_type_1.append(singular)
#       sent_type_1.append(plural)
# with open ('spmf_sentence_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)   
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
##########################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(lfNOUN) 
#     b=np.random.choice(lfnVERBS)
#     c=np.random.choice(lfNOUN)
#     if a==c:
#         continue
#     else: 
#       singular = f"the {a} is {b}ing the {c}"
#       plural= f"the {a}s are {b}ing the {c}s"
#     if singular  and plural in sent_type_1:
#         counter+=1
#         continue
#     else:
#       sent_type_1.append(singular)
#       sent_type_1.append(plural)
# with open ('splf_sentence_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a) 
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
#######################################################
# while True :
#     if len(sent_type_1) ==400:
#         break       
#     a=np.random.choice(nounlist) 
#     b=np.random.choice(futurefVERBS)
#     c=np.random.choice(nounlist)
#     d=pastfVERBS[futurefVERBS.index(b)]
#     if a==c:
#         continue    
#     future = f"the {a} will {b} the {c}"
#     past= f"the {a} {d} the {c}"
#     if future  and past in sent_type_1:     
#         counter+=1
#         continue
#     else:
#       sent_type_1.append(future)
#       sent_type_1.append(past)
# with open ('hffuture_verbs_sentence_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
##########################################################
# while True :
#     if len(sent_type_1) ==400:
#         break
#     a=np.random.choice(nounlist) 
#     b=np.random.choice(futurepVERBS)
#     c=np.random.choice(nounlist)
#     d=pastpVERBS[futurepVERBS.index(b)]
#     if a==c:
#         continue
        
#     future = f"the {a} will {b} the {c}"
#     past= f"the {a} {d} the {c}"
#     if future  and past in sent_type_1:
#         counter+=1
#         continue
#     else: 
#       sent_type_1.append(future)
#       sent_type_1.append(past)
# with open ('hfpast_verbs_sentence_wiki2.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 