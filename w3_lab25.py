s=input("enter 4 digit binsry number:").split(',')
div=[]
for i in s:
    d=int(i,2)
    if(d%5==0):
        div.append(i)
    else:
        print(i,"not divisible by 5")
print("divisible by 5=",div)        


