a = int(input())
i=1
s=0
while i <= a:
    s += 1/(3*i-2)
    i = i + 1
print(f"{s:.5f}")
 