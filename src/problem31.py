nums = list(map(int, input().split()))
 
s=0
for num in nums[:-1] :
        if num >= 0:
                s += num
         
print(s)
 