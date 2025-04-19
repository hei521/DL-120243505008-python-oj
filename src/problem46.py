def s(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
 
n = list(map(int, input().split()))[:-1] 
p = [x for x in n if s(x)]
print(max(p) if p else 'no')