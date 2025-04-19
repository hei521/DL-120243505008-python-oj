n = int(input())
for x in range(6, n+1):
    s = 1
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            s += i + (x//i if i*i!=x else 0)
    if s == x:
        print(x, end=' ')