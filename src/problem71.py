nums = list(map(int, input().split()))  
nums = nums[:nums.index(0)] if 0 in nums else nums 
if not nums:
    print("没有输入有效整数")
else:
    min_val = min(nums)
    min_index = nums.index(min_val)
    print(min_index)