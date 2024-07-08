# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:01:43 2024

@author: cseweb
"""

l1=["s001","s002","s003","s004"]
l2=["aaa","bbb","ccc","ddd"]
l3=[1,2,3,4]
d1={}
#for k in range(4):
# for i in range(k+1):
#    for j in range(i+1):
#        d1.update({l2[i]:l3[j]})
# d2.update({l1[k]:d1})
#print(d2)
for i in range(4):
    a={l2[i]:l3[i]}
    d1[l1[i]]=a
print(d1)
print(len(d1))
