y = int(input())
if y < 0 or y>100:
    print('illegal')
elif y >=90 and y <= 100:
    print('A')
elif y >= 60 and y <=89:
    print('B')
else:
    print('C')