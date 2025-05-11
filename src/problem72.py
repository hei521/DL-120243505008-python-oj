
nums = list(map(int, input().split()))

if 0 in nums:
    nums = nums[:nums.index(0)]
else:
    nums = nums 


if len(nums) > 100:
    nums = nums[:100]  

nums_sorted = sorted(nums)
print(' '.join(map(str, nums_sorted)))