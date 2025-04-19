a = float(input())
if a <= 50:
    c=0.15*a
else:
    c=7.5+(a-50)*0.25
print(int(c) if c==int(c) else c)