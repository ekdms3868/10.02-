a,b=input("").split()
a=int(a)
b=int(b)
c = input("").split()
for i in range(0,a):
    if(b>int(c[i])):
        print(c[i],end=" ")