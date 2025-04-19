a = int(input())
if a <= 1:
    print(0)
else:
    x=1
    for i in range(2,a-1):
        if a % i == 0:
            x=0
            break
    print(x)