
nums = list(map(int, input().split()))

if 0 in nums:
    nums = nums[:nums.index(0)]
else:
    nums = nums  
nums_sorted = sorted(nums)

n = len(nums_sorted)
if n == 0:
    print("没有有效输入")
else:
    if n % 2 == 1:  # 奇数个元素
        median = nums_sorted[n // 2]
    else:  # 偶数个元素
        median = (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2
    print(median)