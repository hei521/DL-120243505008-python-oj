def f(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
 
a,*l=map(int,input().split())
s=0
for i in l:
    if f(i):
        s+=1
print(s)