n=int(input("enter the size"))
l=[]
for i in range(n):
    a=input("enter names")
    l.append(a)
l.sort()
print('second minimum ',l[1])
print('second maximum',l[-2])
    