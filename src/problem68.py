
nums = list(map(int, input().split()))
n = nums[0]
a = nums[1:n+1]

b = a[::-1]

result = [str(b[i]) for i in range(len(b)) if i % 3 == 0]
print(' '.join(result))