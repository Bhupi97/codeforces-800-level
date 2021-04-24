matrix = []
for i in range(5):
    row = input().split()
    matrix.append(row)

    for j in range(5):
        if matrix[i][j] == '1':
            ans = abs(i-2) + abs(j-2)


print(ans)
        
