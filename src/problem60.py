def f(a, i):
    return int(str(a) * i)

a, n = map(int, input().split())
total = 0
for i in range(1, n + 1):
    total += f(a, i)
print(total)