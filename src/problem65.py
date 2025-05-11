def factor_sum(num):
    if num == 1:
        return 0
    total = 1
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if i == num // i:
                total += i
            else:
                total += i + num // i
    return total
 
def find_perfect_numbers(n):
    perfects = []
    for num in range(2, n+1):
        if factor_sum(num) == num:
            perfects.append(str(num))
    return perfects
 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
 
def find_primes(m, n):
    primes = []
    for num in range(max(2, m), n+1):
        if is_prime(num):
            primes.append(str(num))
    return primes
 
m, n = map(int, input().split())
perfect_numbers = find_perfect_numbers(n)
prime_numbers = find_primes(m, n)
 
print(' '.join(perfect_numbers))
print(' '.join(prime_numbers))