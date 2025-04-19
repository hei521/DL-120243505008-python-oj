a ,b = map(int,input().split())
i=0
x=a
while x >= 1:
        if a % x ==0:
                if b % x ==0:
                        k= x
                        break
        x -= 1
print(k)