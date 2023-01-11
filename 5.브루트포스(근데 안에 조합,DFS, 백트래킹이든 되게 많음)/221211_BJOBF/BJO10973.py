import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))

for i in range(N-1, 0, -1): # 맨 뒤 값부터 시작
    if N_list[i-1] > N_list[i]:
        for j in range(N-1, 0, -1): # 다시 맨 뒤 값부터 큰 값찾기
            if N_list[i-1] > N_list[j]:
                N_list[i-1], N_list[j] = N_list[j], N_list[i-1] # 둘 값을 swap
                N_list = N_list[:i] + sorted(N_list[i:], reverse=True)
                print(*N_list)
                exit()
print(-1)
'''

N(1 ≤ N ≤ 10,000)
둘째 줄에 순열
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력
사전순으로 마지막에 오는 순열인 경우에는 -1을 출력
예제 1
4
1 2 3 4
-------
1 2 4 3
예제 2 
5
5 4 3 2 1
---------
-1
'''