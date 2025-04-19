a, *rest = map(int, input().split()) 
m = a
for num in rest:
    if num == 0:
        break
    if num > m:
        m = num
print(m if m != 0 or a == 0 else 0) 