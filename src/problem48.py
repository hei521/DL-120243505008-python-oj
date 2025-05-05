def f(a):
    s=0
    for i in range(1,a+1):
        if a % i == 0 :
            s+=1
    return s
 
a,*l=map(int,input().split())
s=0
for i in l:
    s+=f(i)
print (s)
 