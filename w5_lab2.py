def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

d = {}
while True:
    n = int(input("Enter a number (or -1 to exit): "))
    if n == -1:
        break
    else:
#        l=[]
#       fibo(n)
#       for i in range(n):
#           l.append(fibo(i))
#        d[n] = l
        d[n]=fibo(n)

print(d)
