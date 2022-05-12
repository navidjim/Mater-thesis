# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:06:21 2022

@author: navid
"""

import numpy as np
import random
# subject1=['lion','wolf','tiger','bear']
# object1=['mouse','hunter','dog','chicken']
# verb1=['eat','chase','kill','catch']
# past1=['ate','chased','killed','caught']
# subject2=['student','professor','teacher','researcher']
# object2=['article','letter','book','document']
# verb2=['send','write','post','review']
# past2=['sent','wrote','posted','reviewed']
# subject3=['robot','computer','phone','engineer']
# object3=['program','game','application','code']
# verb3=['run','edit','save','develop']
# past3=['ran','edited','saved','developed']
# subject4=['kid','artist','designer','student']
# object4=['portrait','picture','image','cover']
# verb4=['draw', 'paint' , 'illustrate','design']
# past4=['drew','painted', 'illustrated', 'designed']
# sent_type_1=[]
# sent_type_2=[]
# sent_type_3=[]
# sent_type_4=[]
# sent_=[]

# ###############################pos-neg    
# # while True : 
# #     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3) + len(sent_type_4) >=400:
# #           break
# #     else: 
# #         a1=np.random.choice(subject1) 
# #         b1=np.random.choice(verb1)
# #         c1=np.random.choice(object1)
# #         a2=np.random.choice(subject2) 
# #         b2=np.random.choice(verb2)
# #         c2=np.random.choice(object2)
# #         a3=np.random.choice(subject3) 
# #         b3=np.random.choice(verb3)
# #         c3=np.random.choice(object3)
# #         a4=np.random.choice(subject4) 
# #         b4=np.random.choice(verb4)
# #         c4=np.random.choice(object4)
    
# #         positive1 = f"the {a1} {b1}s the {c1}"
# #         negative1= f"the {a1} does not {b1} the {c1}"
# #         positive2 = f"the {a2} {b2}s the {c2}"
# #         negative2= f"the {a2} does not {b2} the {c2}"
# #         positive3 = f"the {a3} {b3}s the {c3}"
# #         negative3= f"the {a3} does not {b3} the {c3}"
# #         positive4 = f"the {a4} {b4}s the {c4}"
# #         negative4= f"the {a4} does not {b4} the {c4}"
# #         if negative1 and positive1 in sent_type_1:
# #             continue
# #         elif negative2 and positive2 in sent_type_2:
# #             continue
# #         elif negative3 and positive3 in sent_type_3:
# #             continue
# #         elif negative4 and positive4 in sent_type_4:
# #             continue
# #         else:
# #             sent_type_1.extend([positive1,negative1])
# #             sent_type_2.extend([positive2,negative2])
# #             sent_type_3.extend([positive3,negative3])
# #             sent_type_4.extend([positive4,negative4])
        
       
# # sent_=[*sent_type_1, *sent_type_2, *sent_type_3, *sent_type_4]        
# # with open ('pn_sc_fixlen.txt', 'w') as lf:
# #     for a in sent_[:400]:
# #         lf.write("%s \n" %a)
# ############################################################# plur-sing    
# # while True :
# #     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3) + len(sent_type_4) >=400:
# #           break
# #     else: 
# #         a1=np.random.choice(subject1) 
# #         b1=np.random.choice(verb1)
# #         c1=np.random.choice(object1)
# #         a2=np.random.choice(subject2) 
# #         b2=np.random.choice(verb2)
# #         c2=np.random.choice(object2)
# #         a3=np.random.choice(subject3) 
# #         b3=np.random.choice(verb3)
# #         c3=np.random.choice(object3)
# #         a4=np.random.choice(subject4) 
# #         b4=np.random.choice(verb4)
# #         c4=np.random.choice(object4)
# #         sing1= f"the {a1} is {b1}ing the {c1}"
# #         plur1 = f"the {a1}s are {b1}ing the {c1}s"
# #         sing2= f"the {a2} is {b2}ing the {c2}"
# #         plur2 = f"the {a2}s are {b2}ing the {c2}s"
# #         sing3= f"the {a3} is {b3}ing the {c3}"
# #         plur3 = f"the {a3}s are {b3}ing the {c3}s"
# #         sing4= f"the {a4} is {b4}ing the {c4}"
# #         plur4 = f"the {a4}s are {b4}ing the {c4}s"
# #         if plur1 and sing1 in sent_type_1:
# #             continue
# #         elif plur2 and sing2 in sent_type_2:
# #             continue
# #         elif plur3 and sing3 in sent_type_3:
# #             continue
# #         elif plur4 and sing4 in sent_type_4:
# #             continue
# #         else:
# #             sent_type_1.extend([sing1,plur1])
# #             sent_type_2.extend([sing2 ,plur2])
# #             sent_type_3.extend([sing3,plur3])
# #             sent_type_4.extend([sing4,plur4])
        
       
# # sent_=[*sent_type_1, *sent_type_2, *sent_type_3, *sent_type_4]        
# # with open ('sp_sc_fixlen.txt', 'w') as lf:
# #     for a in sent_[:400]:
# #         lf.write("%s \n" %a)
# # print (sent_type_1)
# # #################################################################### act-pas    
# # while True :
# #     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3) + len(sent_type_4) >=400:
# #           break
# #     else: 
# #         a1=np.random.choice(subject1) 
# #         b1=np.random.choice(verb1)
# #         c1=np.random.choice(object1)
# #         d1=past1[verb1.index(b1)]
# #         a2=np.random.choice(subject2) 
# #         b2=np.random.choice(verb2)
# #         c2=np.random.choice(object2)
# #         d2=past2[verb2.index(b2)]
# #         a3=np.random.choice(subject3) 
# #         b3=np.random.choice(verb3)
# #         c3=np.random.choice(object3)
# #         d3=past3[verb3.index(b3)]
# #         a4=np.random.choice(subject4) 
# #         b4=np.random.choice(verb4)
# #         c4=np.random.choice(object4)
# #         d4=past4[verb4.index(b4)]
# #         if d1 == 'ate':
# #                 d1='eaten'
# #         if d2 == 'wrote':
# #                 d2='written'
# #         if d3 == 'ran':
# #                 d3='run'
# #         if d4 == 'drew':
# #                 d4='drawn'
# #         act1 = f"the {a1} {b1}s the {c1}"
# #         pas1= f"the {c1} is {d1} by the {a1}"

# #         act2 = f"the {a2} {b2}s the {c2}"
# #         pas2= f"the {c2} is {d2} by the {a2}"
# #         act3 = f"the {a3} {b3}s the {c3}"
# #         pas3= f"the {c3} is {d3} by the {a3}"
# #         act4 = f"the {a4} {b4}s the {c4}"
# #         pas4= f"the {c4} is {d4} by the {a4}"
# #         if act1 and pas1 in sent_type_1:
# #             continue
# #         elif act2 and pas2 in sent_type_2:
# #             continue
# #         elif act3 and pas3 in sent_type_3:
# #             continue
# #         elif act4 and pas4 in sent_type_4:
# #             continue
# #         else:
# #             sent_type_1.extend([act1,pas1])
# #             sent_type_2.extend([act2,pas2])
# #             sent_type_3.extend([act3,pas3])
# #             sent_type_4.extend([act4,pas4])
# # sent_=[*sent_type_1, *sent_type_2, *sent_type_3, *sent_type_4]        
# # with open ('ap_sc_fixlen.txt', 'w') as lf:
# #     for a in sent_[:400]:
# #         lf.write("%s \n" %a)
# # print (sent_type_1)
# # ################################################################## pas-fut    
# while True :
#     if len(sent_type_1) + len(sent_type_2) + len(sent_type_3) + len(sent_type_4) >=400:
#           break
#     else: 
#         a1=np.random.choice(subject1) 
#         b1=np.random.choice(verb1)
#         c1=np.random.choice(object1)
#         d1=past1[verb1.index(b1)]
#         a2=np.random.choice(subject2) 
#         b2=np.random.choice(verb2)
#         c2=np.random.choice(object2)
#         d2=past2[verb2.index(b2)]
#         a3=np.random.choice(subject3) 
#         b3=np.random.choice(verb3)
#         c3=np.random.choice(object3)
#         d3=past3[verb3.index(b3)]
#         a4=np.random.choice(subject4) 
#         b4=np.random.choice(verb4)
#         c4=np.random.choice(object4)
#         d4=past4[verb4.index(b4)]
    
#         pas1 = f"the {a1} {d1} the {c1}"
#         fut1= f"the {a1} will {b1} the {c1}"
#         pas2 = f"the {a2} {d2} the {c2}"
#         fut2= f"the {a2} will {b2} the {c2}"
#         pas3 = f"the {a3} {d3} the {c3}"
#         fut3= f"the {a3} will {b3} the {c3}"
#         pas4 = f"the {a4} {d4} the {c4}"
#         fut4= f"the {a4} will {b4} the {c4}"
#         if pas1 and fut1 in sent_type_1:
#             continue
#         elif pas2 and fut2 in sent_type_2:
#             continue
#         elif pas3 and fut3 in sent_type_3:
#             continue
#         elif pas4 and fut4 in sent_type_4:
#             continue
#         else:
#             sent_type_1.extend([fut1,pas1])
#             sent_type_2.extend([fut2,pas2])
#             sent_type_3.extend([fut3,pas3])
#             sent_type_4.extend([fut4,pas4])
        
       
# sent_=[*sent_type_1, *sent_type_2, *sent_type_3, *sent_type_4]        
# with open ('fp_sc_fixlen.txt', 'w') as lf:
#     for a in sent_[:400]:
#         lf.write("%s \n" %a)
# print (sent_type_1)


############################################################################################################################
############################################################################################################################
#######                  syntactically correct sentences with random Structure and length                            #######


subject1=['lion','wolf','tiger','bear']
object1=['mouse','hunter','dog','chicken']
cond1=['in the jungle','during the night in the mountains','near the capital city']
verb1=['eat','chase','kill','catch']
pp1=['eaten','chased','killed','cought']
past1=['ate','chased','killed','caught']
subject2=['student','professor','teacher','researcher']
object2=['article','letter','book','document']
cond2=['at school', 'during the class','in an online meeting']
verb2=['send','write','post','review']
pp2=['sent','written','posted','reviewed']
past2=['sent','wrote','posted','reviewed']
subject3=['robot','computer','phone','engineer']
object3=['program','game','application','code']
cond3=['using the memory','online','in paralel']
verb3=['run','edit','save','develop']
past3=['ran','edited','saved','developed']
pp3=['run','edited','saved','developed']
subject4=['kid','artist','designer','student']
object4=['portrait','picture','image','cover']
cond4=['at the gallery',"on the church's ceiling",'in this week art magazine']
verb4=['draw', 'paint' , 'illustrate','design']
past4=['drew','painted', 'illustrated', 'designed']
pp4=['drawn','painted', 'illustrated', 'designed']
sent_type_1=[]
sent_type_2=[]
sent_type_3=[]
sent_type_4=[]
sent_=[]

################################pos-neg    
# while True : 
#     if len(sent_) >=400:
#           break
#     else: 
#         na1=random.sample(subject1,3) 
#         v1=random.sample(verb1,3)
#         nb1=random.sample(object1,3)
#         d1=random.sample(cond1,3)
#         na2=random.sample(subject2,3) 
#         v2=random.sample(verb2,3)
#         nb2=random.sample(object2,3)
#         d2=random.sample(cond2,3)
#         na3=random.sample(subject3,3) 
#         v3=random.sample(verb3,3)
#         nb3=random.sample(object3,3)
#         d3=random.sample(cond3,3)
#         na4=random.sample(subject4,3)
#         v4=random.sample(verb4,3)
#         nb4=random.sample(object4,3)
#         d4=random.sample(cond4,3)
#         myDict={"List1":[na1,v1,nb1,d1],
#                 "List2":[na2,v2,nb2,d2],
#                 "List3":[na3,v3,nb3,d3],
#                 "list4":[na4,v4,nb4,d4]}
#         for l in myDict.values():
#           counter=0
#           for na,v,nb,d in zip(l[0],l[1],l[2],l[3]):
             
             
#                   pos1= f"the {na} {v}s the {nb}"
#                   neg1= f"the {na} does not {v} the {nb}"
#                   if pos1 and neg1 in sent_type_1:
#                       continue
#                   else:
#                       sent_type_1.extend([pos1,neg1])
            
#                   pos2= f"a {na} is {v}ing a {nb} {d}"
#                   neg2= f"the {na} isn't {v}ing the {nb} {d}"
#                   if  pos2 and neg2 in sent_type_2:
#                         continue
#                   else:
#                       sent_type_2.extend([pos2,neg2])   
             
#                   pos3= f"the {na} {v}s the {nb} {d}"
#                   neg3= f"the {na} does not {v} the {nb} {d}"
#                   if  pos3 and neg3 in sent_type_3:
#                         continue
#                   else:
#                       sent_type_3.extend([pos3,neg3] )  
#     sent_=[*sent_type_1, *sent_type_2, *sent_type_3] 
       
# with open ('pn_sc_notfixl.txt', 'w') as lf:
#       for a in sent_[:400]:
#         lf.write("%s \n" %a)
# print (sent_)
############################################################# plur-sing    
# while True : 
#     if len(sent_) >=400:
#           break
#     else: 
#         na1=random.sample(subject1,3) 
#         v1=random.sample(verb1,3)
#         nb1=random.sample(object1,3)
#         d1=random.sample(cond1,3)
#         na2=random.sample(subject2,3) 
#         v2=random.sample(verb2,3)
#         nb2=random.sample(object2,3)
#         d2=random.sample(cond2,3)
#         na3=random.sample(subject3,3) 
#         v3=random.sample(verb3,3)
#         nb3=random.sample(object3,3)
#         d3=random.sample(cond3,3)
#         na4=random.sample(subject4,3)
#         v4=random.sample(verb4,3)
#         nb4=random.sample(object4,3)
#         d4=random.sample(cond4,3)
#         myDict={"List1":[na1,v1,nb1,d1],
#                 "List2":[na2,v2,nb2,d2],
#                 "List3":[na3,v3,nb3,d3],
#                 "list4":[na4,v4,nb4,d4]}
#         for l in myDict.values():
#           counter=0
#           for na,v,nb,d in zip(l[0],l[1],l[2],l[3]):
             
             
#                   sing1 = f"the {na} {v}s the {nb}"
#                   plur1= f"the {na}s {v} the {nb}s"
#                   if sing1 and  plur1 in sent_type_1:
#                       continue
#                   else:
#                       sent_type_1.extend([sing1, plur1])
            
#                   sing2 = f"the {na} is {v}ing the {nb} {d}"
#                   plur2= f"the {na}s are {v}ing the {nb}s {d}"
#                   if sing2 and  plur2 in sent_type_2:
#                         continue
#                   else:
#                       sent_type_2.extend([sing2, plur2])   
             
#                   sing3 = f"the {na} {v}s the {nb} {d}"
#                   plur3= f"the {na}s {v} the {nb}s {d}"
#                   if  sing3 and  plur3 in sent_type_3:
#                         continue
#                   else:
#                       sent_type_3.extend([sing3, plur3] )  
#     sent_=[*sent_type_1, *sent_type_2, *sent_type_3] 
       
# with open ('sp_sc_notfixl.txt', 'w') as lf:
#       for a in sent_[:400]:
#         lf.write("%s \n" %a)
# print (sent_)

# # #################################################################### act-pas 
# while True : 
#     if len(sent_) >=400:
#           break
#     else: 
#         na1=random.sample(subject1,3) 
#         v1=random.sample(verb1,3)
#         nb1=random.sample(object1,3)
#         d1=random.sample(cond1,3)
#         p1=[pp1[verb1.index(v1[0])],pp1[verb1.index(v1[1])],pp1[verb1.index(v1[2])]]
#         na2=random.sample(subject2,3) 
#         v2=random.sample(verb2,3)
#         nb2=random.sample(object2,3)
#         d2=random.sample(cond2,3)
#         p2=[pp2[verb2.index(v2[0])],pp2[verb2.index(v2[1])],pp2[verb2.index(v2[2])]]
#         na3=random.sample(subject3,3) 
#         v3=random.sample(verb3,3)
#         nb3=random.sample(object3,3)
#         d3=random.sample(cond3,3)
#         p3=[pp3[verb3.index(v3[0])],pp3[verb3.index(v3[1])],pp3[verb3.index(v3[2])]]
#         na4=random.sample(subject4,3)
#         v4=random.sample(verb4,3)
#         nb4=random.sample(object4,3)
#         d4=random.sample(cond4,3)
#         p4=[pp4[verb4.index(v4[0])],pp4[verb4.index(v4[1])],pp4[verb4.index(v4[2])]]
#         myDict={"List1":[na1,v1,nb1,d1,p1],
#                 "List2":[na2,v2,nb2,d2,p2],
#                 "List3":[na3,v3,nb3,d3,p3],
#                 "list4":[na4,v4,nb4,d4,p4]}
#         for l in myDict.values():
#           counter=0
#           for na,v,nb,d,p in zip(l[0],l[1],l[2],l[3],l[4]):
             
             
#                   act1 = f"the {na} {v}s the {nb}"
#                   pas1= f"the {nb} is {p} by the {na}"
#                   if act1 and  pas1 in sent_type_1:
#                       continue
#                   else:
#                       sent_type_1.extend([act1, pas1])
            
#                   act2 = f"the {na} is {v}ing the {nb} {d}"
#                   pas2= f"the {nb} is being {p} by the {na} {d}"
#                   if act2 and  pas2 in sent_type_2:
#                         continue
#                   else:
#                       sent_type_2.extend([act2, pas2])   
             
#                   act3 = f"the {na} {v}s the {nb} {d}"
#                   pas3= f"the {nb} is {p} by the {na} {d}"
#                   if  act3 and  pas3 in sent_type_3:
#                         continue
#                   else:
#                       sent_type_3.extend([act3, pas3] )  
#     sent_=[*sent_type_1, *sent_type_2, *sent_type_3] 
       
# with open ('ap_sc_notfixl.txt', 'w') as lf:
#       for a in sent_[:400]:
#         lf.write("%s \n" %a)
# print (sent_)   
       

# ################################################################## pas-fut  
while True : 
    if len(sent_) >=400:
          break
    else: 
        na1=random.sample(subject1,3) 
        v1=random.sample(verb1,3)
        nb1=random.sample(object1,3)
        d1=random.sample(cond1,3)
        p1=[past1[verb1.index(v1[0])],past1[verb1.index(v1[1])],past1[verb1.index(v1[2])]]
        na2=random.sample(subject2,3) 
        v2=random.sample(verb2,3)
        nb2=random.sample(object2,3)
        d2=random.sample(cond2,3)
        p2=[past2[verb2.index(v2[0])],past2[verb2.index(v2[1])],past2[verb2.index(v2[2])]]
        na3=random.sample(subject3,3) 
        v3=random.sample(verb3,3)
        nb3=random.sample(object3,3)
        d3=random.sample(cond3,3)
        p3=[past3[verb3.index(v3[0])],past3[verb3.index(v3[1])],past3[verb3.index(v3[2])]]
        na4=random.sample(subject4,3)
        v4=random.sample(verb4,3)
        nb4=random.sample(object4,3)
        d4=random.sample(cond4,3)
        p4=[past4[verb4.index(v4[0])],past4[verb4.index(v4[1])],past4[verb4.index(v4[2])]]
        myDict={"List1":[na1,v1,nb1,d1,p1],
                "List2":[na2,v2,nb2,d2,p2],
                "List3":[na3,v3,nb3,d3,p3],
                "list4":[na4,v4,nb4,d4,p4]}
        for l in myDict.values():
          counter=0
          for na,v,nb,d,p in zip(l[0],l[1],l[2],l[3],l[4]):
             
             
                  pas1 = f"the {na} {p} the {nb}"
                  fut1= f"the {na} will {v} the {nb}"
                  if pas1 and  fut1 in sent_type_1:
                      continue
                  else:
                      sent_type_1.extend([pas1,fut1])
            
                  pas2 = f"the {na} was {p}ing the {nb} {d}"
                  fut2= f"the {na} will be {v}ing the {nb} {d}"
                  if pas2 and  fut2 in sent_type_2:
                      continue
                  else:
                      sent_type_2.extend([pas2,fut2])   
             
                  pas3 = f"the {na} {p} the {nb} {d}"
                  fut3= f"the {na} will {v} the {nb} {d}"  
                  if  pas3 and  fut3 in sent_type_3:
                      continue
                  else:
                      sent_type_3.extend([pas3, fut3])  
    sent_=[*sent_type_1, *sent_type_2, *sent_type_3] 
       
with open ('pf_sc_notfixl.txt', 'w') as lf:
      for a in sent_[:400]:
        lf.write("%s \n" %a)
print (sent_)   
 
    