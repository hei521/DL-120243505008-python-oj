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
        print("m��n������1��50֮�������")
        return
    
    print(f"������{m}��{n}�еľ���ÿ���ÿո�ָ����س����У���")
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"ÿ�б�������{n}������")
            return
        matrix.append(row)
    
    sum_perimeter = calculate_perimeter_sum(matrix, m, n)
    print(f"�����ܱ�Ԫ��֮��Ϊ��{sum_perimeter}")

if __name__ == "__main__":
    main()