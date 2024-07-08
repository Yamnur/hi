# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:38:47 2024

@author: cseweb
"""

x=int(input("enter x"))
y=int(input("enter y"))
if(x==0 and y==0):
    print("x and y lies in oregin")
elif(x>0 and y>0):
     print("x and y lies in 1st qudrant")
elif(x<0 and y>0):
     print("x and y lies in 2nd qudrant")
elif(x<0 and y<0):
     print("x and y lies in 3rd qudrant")
elif(x>0 and y<0):
     print("x and y lies in 4th qudrant")
else:
    print("not a number")