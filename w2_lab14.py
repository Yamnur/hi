# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:09:28 2024

@author: cseweb
"""

a=int(input("enter number a:"))
b=int(input("enter number b:"))
ch=input("enter choice :\nA-arthmetic optn\nB-bitwise optn\n")
if(ch=='A'):
    c=input("enter choice :\n+ for add\n- for sub\n* for mult\n/ for div\n")
    if(c=='+'):
        print("sum of two numbers=",a+b)
    elif(c=='-'):
        print("sum of two numbers=",a-b)
    elif(c=='*'):
        print("sum of two numbers=",a*b)
    elif(c=='/'):
        print("sum of two numbers=",a/b)
    else:
        print("invalid choice")
elif(ch=="B"):
    c=input("enter choice :\n& for bitAND\n| for bitOR\n ^ for bitXOR\n~ for bitNOT\n")
    if(c=='&'):
        print("bitwise AND =",bin(a&b))
    elif(c=='|'):
        print("bitwise OR =",bin((a|b)))
    elif(c=='^'):
        print("bitwise XOR=",bin((a^b)))
    elif(c=='~'):
        print("bitwise NOT=",bin(~a),bin(~b))
    else:
        print("invalid choice")
else:
    print("invalid choice");