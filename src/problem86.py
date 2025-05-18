def str_len(s):
    length = 0
    for _ in s:
        length += 1
    return length

n = int(input())
if n >= 100:
    print("n must be < 100")
else:
    total = sum(str_len(input().strip()) for _ in range(n))
    print(f"{total/n:.2f}")