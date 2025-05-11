
nums = list(map(int, input().split()))


end_index = nums.index(0) if 0 in nums else len(nums)
numbers = nums[:end_index] 

average = sum(numbers) / len(numbers) if numbers else 0.0

print("{:.6f}".format(average))