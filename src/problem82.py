
n = int(input("请输入矩阵的大小n（n<=50）："))

if n <= 0 or n > 50:
    print("输入的n值不符合要求")
else:
    matrix = []
    print(f"请输入{n}行{n}列的矩阵（每行用空格分隔）：")
    
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"错误：第{i+1}行应输入{n}个数")
            exit()
        matrix.append(row)
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]    
        diagonal_sum += matrix[i][n-1-i]    
    

    if n % 2 == 1:
        center = n // 2
        diagonal_sum -= matrix[center][center]
    
    print("两条对角线元素之和：", diagonal_sum)