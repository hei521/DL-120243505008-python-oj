n = int(input())
if n <= 0 or n >= 100:
    print("输入的n不符合要求")
else:
    fib = [0, 1]
    
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print("斐波那契数列前{}项：".format(n), ' '.join(map(str, fib)))
    
    result = [x for x in fib if x % 3 == 2]
    print("对3取余为2的数：", ' '.join(map(str, result)))