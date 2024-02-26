import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 거듭제곱용 행렬곱셈
def multMat(M1, M2):
    row = len(M1)
    col = len(M2[0])
    result = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(col): # 거듭제곱용은 m * m에서만 가능
                result[i][j] += M1[i][k] * M2[k][j]

    return result

# 거듭제곱
def powerMat(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multMat(x,x), n // 2)
    else:
        return multMat(x, powerMat(multMat(x,x), (n - 1) // 2))
            
if __name__ == "__main__": # 메인문입니다.
    matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    n = 3
    result_matrix = powerMat(matrix1, n)
    
    for row in result_matrix:
        print(row)
    