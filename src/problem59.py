def sum_digits(n): return sum(int(d) for d in str(n))
 
nums = list(map(int, input().split()))
nums = nums[:nums.index(0)] if 0 in nums else nums
res = [x for x in nums if sum_digits(x) % 2 == 1]
print(*res)