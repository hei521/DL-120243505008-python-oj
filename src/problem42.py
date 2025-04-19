b =list(map(int,input().split()))
n=0
x=b[0]
for i in b[0:-1]:
        n+=1
        if i > x:
                x=i
print(n,x)