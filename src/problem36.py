n = int(input())
a, b = 0, 1
 
for _ in range(2, n + 1):
    a, b = b, a + b
 
print("yes" if b % 3 == 0 else "no")