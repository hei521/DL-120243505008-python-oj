a = map(int,input().split())
s=0
p=0
for i in a:
        s+=i
        p+=1
print(s/(p-1))