# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:25:58 2024

@author: cseweb
"""
# prgm to print multiplication table for given number
n=int(input("enter n"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)




# prgm to print multiplication table from n to m
n=int(input("enter n"))
m=int(input("enter m"))
for i in range(n,m+1):
  for j in range(1,11):
    print("%d"%(i*j),end=" ")
  print()
  
  


# prgm to print multiplication table from n to m
n=int(input("enter n"))
m=int(input("enter m"))
for i in range(n,m+1):
  for j in range(1,11):
    print("%d*%d=%d"%(i,j,i*j))
  print()