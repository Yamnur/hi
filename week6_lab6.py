import re
s=input("enter a pancard no")
reg=r'[A-Z]{5}[0-9]{4}[A-Z]'
a=re.search(reg,s)
if a:
    print("valid")
else:
    print("not")