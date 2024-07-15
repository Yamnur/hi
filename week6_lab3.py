n=int(input("enter n"))
unique_words = []
f=open('d.txt','r')
f2=open('key.txt','w')
for i in range(n):
        words = f.readline().split()  
        
        for word in words:
            if word not in unique_words:
                unique_words.append(word) 
for word in unique_words:
        f2.write(word + "\n") 

#n=int(input("enter n"))
#f=open('d.txt','r')
#for i in range(n):
#    x=f.readline()
#    print(x)


