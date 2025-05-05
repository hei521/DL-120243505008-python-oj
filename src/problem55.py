def f(a,b):
    if b == 1:
        return a
    else:
        return a*f(a,b-1)
 
a,b=map(int,input().split())
s=0
for i in range(1,a+1):
   s+=f(i,b)
print(s)