m = int(input())
if m <= 4:
    print(50)
elif m <=8:
    print(50+(m-4)*20)
else:
    print(50+4*20+(m-8)*30)