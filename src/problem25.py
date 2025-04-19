a = int(input())
i=0
while a > 0:
    x=a//2
    a = a-x-2
    i += 1
print(i)