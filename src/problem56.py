def f(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
 
a,b = map(int,input().split())
s=0
for i in range(a,b+1):
    if f(i):
        s+=i
print(s)