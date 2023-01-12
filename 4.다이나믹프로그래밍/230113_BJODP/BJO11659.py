import sys
input = sys.stdin.readline

N, K = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.insert(0,0)
N_sum = [0] * (N + 1)
for i in range(1, N + 1):
    N_sum[i] = N_list[i] + N_sum[i-1]


for _ in range(K):
    i, j = map(int,input().split())
    print(N_sum[j] - N_sum[i - 1])

'''
수의 개수 N과 합을 구해야 하는 횟수 M
N개의 수
M개의 줄에는 합을 구해야 하는 구간 i와 j
예제 입력 1 
5 3
0 5 4 3 2 1
0 5 9 12 14 15
1 3
2 4
5 5
예제 출력 1 
12
9
1
'''