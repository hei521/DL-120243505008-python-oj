m = int(input())
s=0
while m != 0:
    s+=(m%10)
    m=m//10
print(s)