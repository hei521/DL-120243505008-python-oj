n = int(input())
i = 1
s = 0
while i <= n:
    s += 1/i
    i+=1
print(f"{s:.5f}")