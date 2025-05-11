def custom_sort(arr):
    odd = [x for x in arr if x % 2 != 0]
    even = [x for x in arr if x % 2 == 0]
    
    odd_sorted = sorted(odd)
    even_sorted = sorted(even)
    
    return odd_sorted + even_sorted

input_str = input()
nums = list(map(int, input_str.split()))

if 0 in nums:
    nums = nums[:nums.index(0)]
else:
    nums = nums 

sorted_nums = custom_sort(nums)
print(' '.join(map(str, sorted_nums)))