a ,b = map(int, input().split())
c = a - 110
if b > c + 5:
    print('fat')
elif b < c - 5:
    print('thin')
else:
    print('standard')