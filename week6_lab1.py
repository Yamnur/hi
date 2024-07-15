f=open("from.txt","r")
f1=open("vowel.txt","w")
for i in f:
    if i[0] in 'aeiouAEIOU':
       f1.write(i)
