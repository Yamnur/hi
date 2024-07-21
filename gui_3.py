# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:07:54 2024

@author: Admin
"""

'''design a gui to place 2 buttons with text click and click1 onclicking the 1st button display a label
with  text 'python is core programming language
' on pressing 2nd btn dsply msg widget with a text 'covid made india to get into lockdown'
'''
from tkinter import *
def click(k):
    if k==1:        
        l=Label(f,text="python core programming language",bg="green",font=('roman',15,'bold'))
        l.place(x=0,y=0)
    else:
        l=Label(f,text="covid made india to get into lockdown",bg="white",fg='red',font=('roman',15,'bold'))
        l.place(x=0,y=50)
r=Tk()
r.title("hi")
r.geometry('900x900')
r.configure(bg='red')
f=Frame(r,width=500,height=500,bg='skyblue')
f.place(x=10,y=10)
b=Button(f,text='click',command=lambda:click(1))
b1=Button(f,text='click',command=lambda:click(2))
b.place(x=0,y=0)

b1.place(x=0,y=50)
r.mainloop()
