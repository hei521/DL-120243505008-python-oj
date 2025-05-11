def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_series(e):
    total = 1.0  # 前两项1+1
    n = 2        # 从第2项(1/1)开始
    while True:
        fib = fibonacci(n)
        if fib == 0:  # 避免除以0
            term = 0
        else:
            term = 1.0 / fib
        
        if term < e:
            break
        
        total += term
        n += 1
    
    return total

# 主程序
e = float(input())
result = calculate_series(e)
print( result)