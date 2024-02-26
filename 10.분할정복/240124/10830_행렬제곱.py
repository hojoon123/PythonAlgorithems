import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


# 행렬 곱셈
def matrix_mul(arr1, arr2, n):
    result = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tmp = sum(arr1[row][i] * arr2[i][col] for i in range(n))
            result[row][col] = tmp % 1000
    
    return result
# 분할 정복
def power(b, arr, n):
    if b == 1:
        return arr
    elif b % 2 == 0:
        half = power(b // 2, arr, n)
        return matrix_mul(half, half, n)
    else:
        return matrix_mul(arr, power(b-1, arr, n), n)

def main():
    n, b = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(n)]
    
    for rows in power(b, arr, n):
        print(*[row % 1000 for row in rows])
        
    
if __name__ == "__main__":
    main()