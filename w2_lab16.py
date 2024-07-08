# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:49:38 2024

@author: cseweb
"""
n = int(input("Enter n: "))
fib = [0, 1]

for i in range(2, n ):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)
if(n==0):
    print("n is zero")
elif(n==1):
    print(fib[0])
else:
 print("Fibonacci sequence:")
 for j in fib:
    print(j,end="->")
