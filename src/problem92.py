def calculate_perimeter_sum(matrix, m, n):
    if m == 1 and n == 1:  
        return matrix[0][0]
    
    perimeter_sum = 0

    for j in range(n):
        perimeter_sum += matrix[0][j]  
        if m > 1:  
            perimeter_sum += matrix[m-1][j] 
   
    for i in range(1, m-1):
        perimeter_sum += matrix[i][0]  
        if n > 1:  
            perimeter_sum += matrix[i][n-1]  
    
    return perimeter_sum

def main():
    m, n = map(int, input().split())
    if m <= 0 or n <= 0 or m > 50 or n > 50:
        print("m和n必须是1到50之间的整数")
        return
    
    print(f"请输入{m}行{n}列的矩阵（每行用空格分隔，回车换行）：")
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"每行必须输入{n}个整数")
            return
        matrix.append(row)
    
    sum_perimeter = calculate_perimeter_sum(matrix, m, n)
    print(f"矩阵周边元素之和为：{sum_perimeter}")

if __name__ == "__main__":
    main()