# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:56:16 2024

@author: cseweb
"""

n=int(input("enter n"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    


#z pattern
for i in range(n):
        for j in range(n):
            if((i == 0) or(i == n-1) or(i+j == n-1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


#T pattern
for i in range(n):
        for j in range(n):
            if ((i == 0) or(j == n//2)):
            
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
