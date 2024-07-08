# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:30:48 2024

@author: cseweb
"""


a=int(input("enter number a:"))
b=int(input("enter number b:"))
if(a%2!=0 and b%2!=0):
    if(a!=b):
        a,b=b,a
        print("a=",a,"b=",b)
    else:
         print("both numbers are equal")
         print("fact a=b=",factorial(a))
         
elif(a%2==0 and b%2==0):
    if(a==b):
        
        print("fact a=b=",factorial(a))
    else:
        if(a>b):
            print("large=",a)
        else:
            print("large=",b)
else:

    print("fact a=%d\nfact b=%d"%(factorial(a),factorial(b)))
  
    
    
