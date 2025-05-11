
nums = list(map(int, input().split()))
numbers = nums[:nums.index(0)] if 0 in nums else nums


print(max(numbers) if numbers else 0)