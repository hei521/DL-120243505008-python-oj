n_and_numbers = list(map(int, input().split()))
n = n_and_numbers[0]
numbers = n_and_numbers[1:n+1]

divisible_by_3 = [str(num) for num in reversed(numbers) if num % 3 == 0]
print(' '.join(divisible_by_3))

index_3_multiple = [str(numbers[i]) for i in range(len(numbers)-1, -1, -1) if i % 3 == 0]
print(' '.join(index_3_multiple))