n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

tetromino = [[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]], 
[[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]], 
[[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]], 
[[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]], 
[[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]], 
[[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]], 
[[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]], 
[[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]], 
[[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]], 
[[0, 1], [0, 2], [-1, 1]]]

result = 0
for i in range(n):
    for j in range(m):
        for k in tetromino:
            try:
                sum_n = array[i][j] + array[i + k[0][0]][j + k[0][1]] + array[i + k[1][0]][j + k[1][1]] + array[i + k[2][0]][j + k[2][1]]
            except:
                sum_n = 0
            result = max(result, sum_n)
print(result)