import math
a , b ,c = map(int,input().split())
m=b*b - 4*a*c
if  m < 0:
    print('none')
elif m == 0:
    x=-b/(2*a)
    print(int(x) if x == int(x) else x)
else:
    x=math.sqrt(m)
    q=(-b-x)/(2*a)
    w=(-b+x)/(2*a)
    print(f"{int(q) if q.is_integer() else q} {int(w) if w.is_integer() else w}")