a,*q = list(map(int,input().split()))
 
r= []
for l in q:
        if l <= 1000:
                x=0
        elif l <= 3000:
                x=0.03*l
        elif l <=5000:
                x=0.04*l
        else:
                x=0.06*l
        f = f"{x:g}"
        r.append(str(f))
print(' '.join(r))
         