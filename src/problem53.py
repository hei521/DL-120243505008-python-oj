def f(a,b):
    for i in range(min(a,b),-1,-1):
        if b % i == 0:
            if a % i == 0:
                break
    return i
 
a,*l=map(int,input().split())
m=0
for i in range(a):
    x = l[2*i]
    y = l[2*i+1]
    m+=f(x,y)
print(m)