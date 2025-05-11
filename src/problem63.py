def digital_root(n):
    if n < 10:
        return n
    sum_digits = sum(int(digit) for digit in str(n))
    return digital_root(sum_digits)
 
input_numbers = list(map(int, input().split()))
n = input_numbers[0]
numbers = input_numbers[1:]
 
for num in numbers:
    print(digital_root(num), end=' ')
print()  