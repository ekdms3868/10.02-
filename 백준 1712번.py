a,b,c=input("").split()
a=int(a)
b=int(b)
c=int(c)
d=0
for x in range(1,100):
    d=(c*x)-a-(b*x)
    if d<=0:
        print("-1")
    else:
        break
print(x)