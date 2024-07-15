f = open("month.txt", "r")
a = f.readlines()
l = []
for i in range(len(a)):
    if i%2==0:
        l.append(a[i])
print(l)
f1 = open("k.txt", "w")
for line in l:
    f1.write(line)
f.close()
f1.close()
