def rev(n):
    if n == 0: return 0
    s = -1 if n < 0 else 1
    return int(str(abs(n))[::-1]) * s
 
nums = list(map(int, input().split()))
nums = nums[:nums.index(0)] if 0 in nums else nums 
total = sum(rev(num) for num in nums)
print( total)