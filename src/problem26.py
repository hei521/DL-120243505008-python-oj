m = list(map(int,input().split()))
s = m[1:]
for i in s:
    if i < 60:
        print('Fail')
    else:
        print('Pass')