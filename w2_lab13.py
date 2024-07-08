# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:52:24 2024

@author: cseweb
"""

s=input("enetr a string ")
if(s.isalpha()):
    print("string containing only alphabet")
    if(s.isupper()):
        print("string is in upper case")
    else:
         print("string is in lower case")
elif(s.isdigit()):
    print("string containing only digit")
    sum=0
    for i in s:
        sum+=int(i)
    print("sum of digit=",sum)
elif(s.isalnum()):
    print("alphanumeric")
    sum=0
    for i in s:
      if(i.isdigit()):
        sum+=int(i)
    print("sum of digit in alnum=",sum)
else:
    print("string containing special char");
    c=0;
    for i in s:
        if(not i.isalpha() and not i.isdigit()):
            c=c+1;
    print("total no.of special char=",c)
        