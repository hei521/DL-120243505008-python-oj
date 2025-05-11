
matrix = []
print()


for i in range(5):
    row = list(map(int, input().split()))
    if len(row) != 5:
        print(f"错误：第{i+1}行应输入5个数")
        exit()
    matrix.append(row)


saddle_points = []
for i in range(5):
    row_max = max(matrix[i])
    max_indices = [j for j, x in enumerate(matrix[i]) if x == row_max]
    
    for j in max_indices:
        column = [matrix[k][j] for k in range(5)]
        if row_max == min(column):
            saddle_points.append((i, j, row_max))

if saddle_points:
    print()
    for point in saddle_points:
        print(f"({point[0]}, {point[1]}, {point[2]})")
else:
    print("矩阵中没有鞍点")