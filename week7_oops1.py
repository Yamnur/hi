# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:50:43 2024

@author: cseweb
"""

class book:
    def __init__(self,name,aut,price):
        self.__title=name
        self.__author=aut
        self.__price=price
    def display(self):
        if self.__title[0]=='D' or self.__title[0]=='d':
           
            print(f"book {i+1} details" )
            print("title of the book:",self.__title)
            print("author of the book:",self.__author)
            print(f"price of the book:{self.__price}\n")
n=int(input("enter n "))
for i in range(n):
    name=input("enter book name:")
    author=input("enter author name:")
    price=float(input("enter price of book:"))
    d=book(name,author,price)
    d.display()      
