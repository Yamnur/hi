# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:31:14 2024

@author: cseweb
"""

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"name = {self.name}\nage = {self.age}\n")
    
    def __eq__(self, other):
        if isinstance(other, person):
            return self.name == other.name and self.age == other.age
        return False

p1 = person("abc", 23)
p2 = person("xyz", 23)

if p1 == p2:
    print("identical")
    p1.display()
else:
    print("not identical\n")
    p1.display()
    p2.display()
    
#class person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def display():
#        print(f"name ={name}\ngage={age}")
#p1=person("abc",23)
#p2=person("xyz",23)
#if p1==p2:
#    p1.display()
#else:  
#    print("not")
#    
#    
