def f(a,b):
    s=0
    if a > b :
        return 0
    for i in range(a,b+1):
        if i % 2 == 1:
            s+=i
    return s
 
a,*l = map(int,input().split())
m=0
for i in range(a):
    a=l[2*i]
    b=l[2*i+1]
    if f(a,b)>= m:
        m=f(a,b)
print (m)