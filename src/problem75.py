n = int(input())
if n <= 0 or n >= 100:
    print("�����n������Ҫ��")
else:
    fib = [0, 1]
    
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print("쳲���������ǰ{}�".format(n), ' '.join(map(str, fib)))
    
    result = [x for x in fib if x % 3 == 2]
    print("��3ȡ��Ϊ2������", ' '.join(map(str, result)))