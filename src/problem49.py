def f(a):
    if a==1 or a==0:
        return a
    else:
        return f(a-1)+f(a-2)
 
 
a,b= map(int,input().split())
r=[]
i=0
while True:
    if f(i)>=b:
        break
    elif f(i)>a:
        r.append(str(f(i)))
    i += 1
print(' '.join(r))