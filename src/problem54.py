def f(a,b):
    if b == 1:
        return a
    else:
        return a*f(a,b-1)
 
a,b=map(float,input().split())
s=f(a,b)
print(f"{s:g}")