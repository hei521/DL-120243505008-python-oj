
n = int(input("���������Ĵ�Сn��n<=50����"))

if n <= 0 or n > 50:
    print("�����nֵ������Ҫ��")
else:
    matrix = []
    print(f"������{n}��{n}�еľ���ÿ���ÿո�ָ�����")
    
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"���󣺵�{i+1}��Ӧ����{n}����")
            exit()
        matrix.append(row)
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]    
        diagonal_sum += matrix[i][n-1-i]    
    

    if n % 2 == 1:
        center = n // 2
        diagonal_sum -= matrix[center][center]
    
    print("�����Խ���Ԫ��֮�ͣ�", diagonal_sum)