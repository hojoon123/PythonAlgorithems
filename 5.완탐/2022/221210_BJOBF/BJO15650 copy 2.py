import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = []
def dfs(start):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(start,N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)
'''
1 2 가 들어가 있음 여기부터 시작해서 1 2 1 3 1 4 2 1 이렇게 가야됨
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
(1 ≤ M ≤ N ≤ 8)
예제 입력 1 
3 1
예제 출력 1 
1
2
3
'''