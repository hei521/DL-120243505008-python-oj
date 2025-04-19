a = int(input())
s=[]
d=0
for i in range(2,a+1):
        x=2
        l=0
        while x<i:
                if i % x ==0:
                        l=1
                        break
                x+=1
        if l==0:
                s.append(str(i))
                d+=1
print(' '.join(s))
print(d)