import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
numbers = [i for i in range(1,N+1)]
visited = [False] * N
arr = []
def dfs():
    if len(arr)==N:
        print(*arr)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(numbers[i])
            dfs()
            visited[i] = False
            arr.pop()
        
dfs()
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