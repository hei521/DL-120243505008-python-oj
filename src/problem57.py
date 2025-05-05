def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return a * b // gcd(a, b)
 
n, *rest = map(int, input().split())
total = 0
for i in range(n):
    a = rest[2*i]
    b = rest[2*i+1]
    total += lcm(a, b)
 
print(total)