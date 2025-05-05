def fac(a):
    if a == 0:
        return 1
    else:
        return a*fac(a-1)
 
a,*l=map(int,input().split())
s=0
for i in l:
    s+=fac(i)
s=s/a
print(int(s) if s==int(s) else s)