def isodd(num):
    return num % 2 != 0
 
nums = list(map(int, input().split()))
numbers = [num for num in nums if num != 0]  
 
odd_numbers = [num for num in numbers if isodd(num)]
odd_count = len(odd_numbers)
 
print(' '.join(map(str, odd_numbers)))
print(odd_count)