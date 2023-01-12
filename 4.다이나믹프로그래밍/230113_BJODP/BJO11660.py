import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
sum_arr = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    arr[i][1 : N + 1] = [*map(int, input().split())]


for i in range(1, N + 1):
    for j in range(1, N + 1):
            sum_arr[i][j] = arr[i][j] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]



for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    ans = sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1]
    print(ans)

'''
표의 크기 N과 합을 구해야 하는 횟수 M
N개의 줄에는 표에 채워져 있는 수
M개의 줄에는 네 개의 정수 x1, y1, x2, y2
M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력
예제 입력 1 
4 3

1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

2 2 3 4
3 4 3 4
1 1 4 4
예제 출력 1 
27
6
64
'''