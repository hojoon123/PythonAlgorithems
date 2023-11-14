import sys
input = sys.stdin.readline()

def multMat(arr1, arr2):
    N = len(arr1)
    # 곱셉 결과를 저장할 2차원 리스트
    result = [[0] * N for _ in range(N)]
    # 행렬 곱셈 연산 수행
    for row in range(N):
        for col in range(N):
            result[row][col] = sum(arr1[row][i] * arr2[i][col] for i in range(N)) 
            print(result)           
    return result

def powerMat(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multMat(x,x), n // 2)
    else:
        return multMat(x, powerMat(multMat(x,x), (n - 1) // 2))
    
if __name__ == "__main__":
    x = [[1,2,3,4],
         [5,6,7,8],
         [1,2,3,4],
         [5,6,7,8]]
    print(powerMat(x, 5))