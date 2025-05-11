
m = int(input("请输入矩阵的行数m（m<=50）："))
n = int(input("请输入矩阵的列数n（n<=50）："))


if m <= 0 or m > 50 or n <= 0 or n > 50:
    print("输入的行列数不符合要求")
else:
    matrix = []
    print(f"请输入{m}行{n}列的矩阵（每行用空格分隔）：")
    
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"错误：第{i+1}行应输入{n}个数")
            exit()
        matrix.append(row)
    
    row_sums = [sum(row) for row in matrix]
    
    col_sums = [sum(matrix[i][j] for i in range(m)) for j in range(n)]

    print("各行元素和：", ' '.join(map(str, row_sums)))
    print("各列元素和：", ' '.join(map(str, col_sums)))