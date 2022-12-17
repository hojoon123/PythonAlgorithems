import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
result = 1e9
visited = [False] * (N + 1)

def solve(depth, idx):
    global result
    if depth == (N // 2): # N // 2 번만큼 재귀를 돌면
        start, link = 0, 0 #start팀과 link팀 0으로 선언
        for i in range(N): 
            for j in range(i + 1, N):
                if visited[i] and visited[j]:
                    start += (arr[i][j] + arr[j][i])
                elif not visited[i] and not visited[j]:
                    link += (arr[i][j] + arr[j][i])
        
        result = min(result, abs(start - link))
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False

solve(0, 0)
print(result)
                
'''
1 2 1 3 1 4
1 2 
돌면서 i가 같을 때 제외 
arr[i][j] + arr[j][i]
N(4 ≤ N ≤ 20, N은 짝수)
예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
예제 출력 1 
0
예제 입력 2 
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
예제 출력 2 
2
'''