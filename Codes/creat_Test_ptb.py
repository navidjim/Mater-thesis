# # -*- coding: utf-8 -*-
# """
# Created on Sat Jan 22 22:38:50 2022

# @author: navid
# """
import numpy as np
############################### ptb ###############################
hfNOUN = ['house', 'chief', 'oil', 'magazine','drug','gas','image']
hfnVERBS = ['clear', 'allow', 'replace','plan','sell','manage']
hfnPVEBS=['cleared','allowed','replaced','planed','sold','managed']
mfNOUN=['author','baby','dog','god','lion','pencil','text']
mfnVERBS=['say','keep','name','know','get','produce']
mfnPVEBS=['said','kept','named','known','gotten','produced']
lfNOUN=['piano','pepsi','thief','rocket','robot','widow','ufo']
lfnVERBS=['play','lead','catch','launch','build','earn']
lfnPVEBS=['played','led','cought','launched','built','earned']

  #frequent future verbs 
futurefVERBS=['have','take','make','sell','help','receive','become']
pastfVERBS=['had','took','made','sold','helped','received','became']
# frequent past verbs 
futurepVERBS=['begin','rise','make','take','add','post','ask']
pastpVERBS=['began','rose','made','took','added','posted','asked']
nounlist=['dr','chief','image','oil','magazine','card']
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
# with open ('hf_pnsentece_ptb.txt', 'w') as lf:
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
# with open ('mf_pnsentece_ptb.txt', 'w') as lf:
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
# with open ('lf_npsentece_ptb.txt', 'w') as lf:
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
# with open ('hfap_sentece_ptb.txt', 'w') as hf:
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
# with open ('mfap_sentece_ptb.txt', 'w') as hf:
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
# with open ('lfap_sentece_ptb.txt', 'w') as hf:
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
# with open ('sphf_sentence_ptb.txt', 'w') as hf:
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
# with open ('spmf_sentence_ptb.txt', 'w') as hf:
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
# with open ('splf_sentence_ptb.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a) 
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
#######################################################
while True :
    if len(sent_type_1) ==400:
        break       
    a=np.random.choice(nounlist) 
    b=np.random.choice(futurefVERBS)
    c=np.random.choice(nounlist)
    d=pastfVERBS[futurefVERBS.index(b)]
    if a==c:
        continue    
    future = f"the {a} will {b} the {c}"
    past= f"the {a} {d} the {c}"
    if future  and past in sent_type_1:     
        counter+=1
        continue
    else:
      sent_type_1.append(past)
      sent_type_1.append(future)
with open ('pf_in_notfix.txt', 'w') as hf:
    for a in sent_type_1:
        hf.write("%s \n" %a)
print (sent_type_1)
print (counter)  
print(len(sent_type_1)) 
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
# with open ('hfpast_verbs_sentence_ptb.txt', 'w') as hf:
#     for a in sent_type_1:
#         hf.write("%s \n" %a)
# print (sent_type_1)
# print (counter)  
# print(len(sent_type_1)) 
######################################################## Not fixed length control & SEMANTICALLY INCORRECT ######################
############################################################################################### 

# NOUN = ['house', 'chief', 'oil', 'magazine','drug','gas','image','author','baby','dog','god','lion','pencil','text','piano','pepsi','thief','rocket','robot','widow','ufo']
# VERB = ['clear', 'allow', 'replace','plan','sell','manage','say','keep','name','know','get','produce','play','lead','launch','build','earn']
# PP=['cleared','allowed','replaced','planed','sold','managed','said','kept','named','known','gotten','produced','played','led','launched','built','earned']
# PVERBS=['cleared','allowed','replaced','planed','sold','managed','said','kept','named','knew','got','produced','played','led','launched','built','earned']
# NCLAUSE=['in the city','in the live show','as a mission during the war','in europe','in the building around the corner']
# #frequent future verbs 
# # futurefVERBS=['have','take','make','sell','help','receive','become']
# # pastfVERBS=['had','took','made','sold','helped','received','became']
# # frequent past verbs 
# # futurepVERBS=['begin','rise','make','take','add','post','ask']
# # pastpVERBS=['began','rose','made','took','added','posted','asked']
# # nounlist=['dr','chief','image','oil','magazine','card']
# sent_type_1 =[] 
# sent_type_2 =[] 
# sent_type_3 =[] 
# sent_type_4 =[] 
# sent_=[]
# count=0
######################################################################################################## POS-NEG
# while True : 
#     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3) + len(sent_type_4) >=400:
#           break  
#     else:
#         a1=np.random.choice(NOUN) 
#         b1=np.random.choice(VERB)
#         c1=np.random.choice(NOUN)
#         a2=np.random.choice(NOUN) 
#         c2=np.random.choice(NOUN)
#         a3=np.random.choice(NOUN) 
#         b3=np.random.choice(VERB)
#         c3=np.random.choice(NOUN)
#         d3=np.random.choice(NCLAUSE)
#         a4=np.random.choice(NOUN) 
#         b4=np.random.choice(VERB)
#         c4=np.random.choice(NOUN)
#         d4=np.random.choice(NCLAUSE)
        
#         while True:
#             if  a1==c1:
#                 a1=np.random.choice(NOUN)
#                 c1=np.random.choice(NOUN)
#             else:
#                 break
        
#         while True:
#             if  a2==c2:
#                 a2=np.random.choice(NOUN)
#                 c2=np.random.choice(NOUN)
#             else:
#                 break
            
#         while True:
#             if  a3==c3:
#                 a3=np.random.choice(NOUN)
#                 c3=np.random.choice(NOUN)
#             else:
#                 break
            
#         while True:
#             if  a4==c4:
#                 a4=np.random.choice(NOUN)
#                 c4=np.random.choice(NOUN)
#             else:
#                 break
        # positive1 = f"the {a1} {b1}s the {c1}"
        # negative1 = f"the {a1} does not {b1} the {c1}"
        # positive2 = f"the {a2} is {c2}"
        # negative2 = f"the {a2} isn't the {c2}"
        # positive3 = f"the {a3} is {b3}ing the {c3} {d3}"
        # negative3 = f"the {a3} isn't {b3}ing the {c3} {d3}"
        # positive4 = f"the {a4} {b4}s the {c4} {d4}"
        # negative4 = f"the {a4} does not {b4} the {c4} {d4}"
  
#         sent_type_1.extend([positive1,negative1])
#         sent_type_2.extend([positive2,negative2])
#         sent_type_3.extend([positive3,negative3])
#         sent_type_4.extend([positive4,negative4])
#         sent_type1=set(sent_type_1)
#         sent_type2=set(sent_type_2)
#         sent_type3=set(sent_type_3)
#         sent_type4=set(sent_type_4)
# sent_=[*sent_type_1, *sent_type_2, *sent_type_4, *sent_type_4]       
# with open ('pn_incorrect_not_fix_ptb.txt', 'w') as hf:
#     for a in sent_:
#         hf.write("%s \n" %a)
# print (sent_)
# print(len(sent_)) 
# the N  V the N
# the N not V the N
# the N is N
# the N isnt N
# the N is v ing the N phrase_condition
# the N isn't  v ing the N phrase_condition
# the N v the N  phrase_condition
# the N not v the N  phrase_condition

######################################################################################################## ACT-PAS
# counter=0

# while True: 
    
#     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3)>=400:
#         break  
#     else:
#         a1=np.random.choice(NOUN) 
#         b1=np.random.choice(VERB)
#         c1=np.random.choice(NOUN)
#         d1=np.random.choice(NCLAUSE)
#         p1=PP[VERB.index(b1)]
#         a2=np.random.choice(NOUN) 
#         b2=np.random.choice(VERB)
#         c2=np.random.choice(NOUN)
#         d2=np.random.choice(NCLAUSE)
#         p2=PP[VERB.index(b2)]
#         a3=np.random.choice(NOUN) 
#         b3=np.random.choice(VERB)
#         c3=np.random.choice(NOUN)
#         d3=np.random.choice(NCLAUSE)
#         p3=PP[VERB.index(b3)]
#         # a4=np.random.choice(NOUN) 
#         # b4=np.random.choice(VERB)
#         # c4=np.random.choice(NOUN)
#         # d4=np.random.choice(NCLAUSE)
#         # p4=PP[VERB.index(b4)]
#         while True:
#             if a1==c1:
#                 a1=np.random.choice(NOUN)
#                 c1=np.random.choice(NOUN)
#             else:
#                 break
        
#         while True:
#             if  a2==c2:
#                 a2=np.random.choice(NOUN)
#                 c2=np.random.choice(NOUN)
#             else:
#                 break
            
#         while True:
#             if  a3==c3:
#                 a3=np.random.choice(NOUN)
#                 c3=np.random.choice(NOUN)
#             else:
#                 break
        # act1 = f"the {a1} {b1}s the {c1}"
        # pas1= f"the {c1} is {p1} by the {a1}"
        # act2 = f"the {a2} is {b2}ing the {c2} {d2}"
        # pas2= f"the {c2} is being {p2} by the {a2} {d2}"
        # act3 = f"the {a3} {b3}s the {c3} {d3}"
        # pas3= f"the {c3} is {p3} by the {a3} {d3}"
#         sent_type_1.extend([act1,pas1])
#         sent_type_2.extend([act2,pas2])
#         sent_type_3.extend([act3,pas3])     
#         sent_type1=set(sent_type_1)
#         sent_type2=set(sent_type_2)
#         sent_type3=set(sent_type_3)
   
      
# sent_=[*sent_type_1, *sent_type_2, *sent_type_3,]
# with open ('ap_incorrect_not_fix_ptb.txt', 'w') as hf:
    
#     for a in sent_[:400]:
#         counter=counter+1
#         hf.write("%s \n" %a)
# print (sent_)
# print(len(sent_)) 
# # the N V the N2
# # the N2 is pV by the N
# # the N is v ing the N phrase_condition
# # the N2 is being pv by the N phrase_condition
# # the N v the N phrase_condition
# # the N2 is pv by the N  phrase_condition
######################################################################################################## sing-plur
# counter=0
# while True : 
  
#     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3)>=400:
#           break  
#     else:
#         a1=np.random.choice(NOUN) 
#         b1=np.random.choice(VERB)
#         c1=np.random.choice(NOUN)
#         d1=np.random.choice(NCLAUSE)
#         p1=PP[VERB.index(b1)]
#         a2=np.random.choice(NOUN) 
#         b2=np.random.choice(VERB)
#         c2=np.random.choice(NOUN)
#         d2=np.random.choice(NCLAUSE)
#         p2=PP[VERB.index(b2)]
#         a3=np.random.choice(NOUN) 
#         b3=np.random.choice(VERB)
#         c3=np.random.choice(NOUN)
#         d3=np.random.choice(NCLAUSE)
#         p3=PP[VERB.index(b3)]
#         # a4=np.random.choice(NOUN) 
#         # b4=np.random.choice(VERB)
#         # c4=np.random.choice(NOUN)
#         # d4=np.random.choice(NCLAUSE)
#         # p4=PP[VERB.index(b4)]
#         while True:
#             if a1==c1:
#                 a1=np.random.choice(NOUN)
#                 c1=np.random.choice(NOUN)
#             else:
#                 break
        
#         while True:
#             if a2==c2:
#                 a2=np.random.choice(NOUN)
#                 c2=np.random.choice(NOUN)
#             else:
#                 break
            
#         while True:
#             if a3==c3:
#                 a3=np.random.choice(NOUN)
#                 c3=np.random.choice(NOUN)
#             else:
#                 break
            
     
      
        # sing1 = f"the {a1} {b1}s the {c1}"
        # plur1= f"the {a1}s {b1} the {c1}s"
        # sing2 = f"the {a2} is {b2}ing the {c2} {d2}"
        # plur2= f"the {a2}s are {b2}ing the {c2}s {d2}"
        # sing3 = f"the {a3} {b3}s the {c3} {d3}"
        # plur3= f"the {a3}s {b3} the {c3}s {d3}"
            
#         sent_type_1.extend([sing1,plur1])
#         sent_type_2.extend([sing2,plur2])
#         sent_type_3.extend([sing3,plur3])
       
# sent_=[*sent_type_1, *sent_type_2, *sent_type_3]
# with open ('sp_incorrect_not_fix_ptb.txt', 'w') as hf:
#     for a in sent_[:400]:
#         counter=counter+1
#         hf.write("%s \n" %a)
# print (sent_)
# print(len(sent_)) 
# the N V the N2
# the Ns V the N2s
# the N is v ing the N phrase_condition
# the N are v ing the Ns phrase_condition
# the n v the N phrase_condition
# the Ns v the Ns phrase_condition
######################################################################################################## fut-pas
# counter=0
# while True : 
  
#     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3)>=400:
#           break  
#     else:
#         a1=np.random.choice(NOUN) 
#         b1=np.random.choice(VERB)
#         c1=np.random.choice(NOUN)
#         d1=np.random.choice(NCLAUSE)
#         p1=PVERBS[VERB.index(b1)]
#         a2=np.random.choice(NOUN) 
#         b2=np.random.choice(VERB)
#         c2=np.random.choice(NOUN)
#         d2=np.random.choice(NCLAUSE)
#         p2=PVERBS[VERB.index(b2)]
#         a3=np.random.choice(NOUN) 
#         b3=np.random.choice(VERB)
#         c3=np.random.choice(NOUN)
#         d3=np.random.choice(NCLAUSE)
#         p3=PVERBS[VERB.index(b3)]
#         # a4=np.random.choice(NOUN) 
#         # b4=np.random.choice(VERB)
#         # c4=np.random.choice(NOUN)
#         # d4=np.random.choice(NCLAUSE)
#         # p4=PP[VERB.index(b4)]
#         while True:
#             if a1==c1:
#                 a1=np.random.choice(NOUN)
#                 c1=np.random.choice(NOUN)
#             else:
#                 break
        
#         while True:
#             if a2==c2:
#                 a2=np.random.choice(NOUN)
#                 c2=np.random.choice(NOUN)
#             else:
#                 break
            
#         while True:
#             if a3==c3:
#                 a3=np.random.choice(NOUN)
#                 c3=np.random.choice(NOUN)
#             else:
#                 break
            
     
      
#         sing1 = f"the {a1} {p1} the {c1}"
#         plur1= f"the {a1} will {b1} the {c1}"
#         sing2 = f"the {a2} was {b2}ing the {c2} {d2}"
#         plur2= f"the {a2} will be {b2}ing the {c2} {d2}"
#         sing3 = f"the {a3} {p3} the {c3} {d3}"
#         plur3= f"the {a3} will {b3} the {c3} {d3}"
            
#         sent_type_1.extend([plur1,sing1])
#         sent_type_2.extend([plur2,sing2])
#         sent_type_3.extend([plur3,sing3])

# sent_=[*sent_type_1, *sent_type_2, *sent_type_3]
# with open ('fp_incorrect_not_fix_ptb.txt', 'w') as hf:
#     for a in sent_[:400]:
#         counter=counter+1
#         hf.write("%s \n" %a)
# print (sent_)
# print(len(sent_)) 
# print(counter)
# the N pV the N2
# the N will V the N2
# the N was v ing the N phrase_condition
# the N will be v ing the Ns phrase_condition
# the n  v the N phrase_condition
# the Ns will v the Ns phrase_condition
#########################################################################################################

