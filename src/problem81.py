
m = int(input("��������������m��m<=50����"))
n = int(input("��������������n��n<=50����"))


if m <= 0 or m > 50 or n <= 0 or n > 50:
    print("�����������������Ҫ��")
else:
    matrix = []
    print(f"������{m}��{n}�еľ���ÿ���ÿո�ָ�����")
    
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"���󣺵�{i+1}��Ӧ����{n}����")
            exit()
        matrix.append(row)
    
    row_sums = [sum(row) for row in matrix]
    
    col_sums = [sum(matrix[i][j] for i in range(m)) for j in range(n)]

    print("����Ԫ�غͣ�", ' '.join(map(str, row_sums)))
    print("����Ԫ�غͣ�", ' '.join(map(str, col_sums)))