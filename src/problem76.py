def sieve_of_eratosthenes(m, n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(m, n + 1) if is_prime[i]]
    return primes

m, n = map(int, input().split())

if m < 1 or n >= 100 or m > n:
    print("输入范围无效")
else:
    primes = sieve_of_eratosthenes(m, n)
    if primes:
        print(f"[{m},{n}]范围内的素数：", ' '.join(map(str, primes)))
    else:
        print(f"[{m},{n}]范围内没有素数")