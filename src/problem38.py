n = int(input())
s = 0
 
while n > 0:
    d = n % 10
    if d % 2 == 0: 
        s += d
    n = n // 10
 
print(s)
 