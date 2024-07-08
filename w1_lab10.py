# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:12:05 2024

@author: cseweb
"""

n=5
l=[]
print("enter 5 sub marks")
for i in range(n):
    k=int(input())
    l.append(k)
sum=0
for i in l:
    sum=sum+i
per=sum/n
if(per>=90):
    print("grade S")
elif(per>=80):
    print("grade A")
elif(per>=70):
    print("grade B")
elif(per>=60):
    print("grade C")
elif(per>=50):
    print("grade D")
else:
    print("grade F")