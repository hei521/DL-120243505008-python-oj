a,*b = map(int,input().split())
q,w = 0,0
 
for i in b:
        if i % 2 ==0:
                w += i**3
        elif i % 2!=0:
                q += i*i
print(q,w)