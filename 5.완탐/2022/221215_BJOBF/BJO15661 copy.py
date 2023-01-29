import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())
ans = []
startTeam = []
linkTeam = []
arr = [list(map(int, input().split())) for _ in range(n)]

# 2 ^ 20 dfs
def dfs(start, link, cnt):
    if cnt == n:
        if start and link:
            ans.append(abs(start-link))
        return
    
    temp = 0
    startTeam.append(cnt)
    for i in startTeam:
        temp += arr[cnt][i]
        temp += arr[i][cnt]
    dfs(start+temp,link,cnt+1)
    startTeam.pop()

    temp = 0
    linkTeam.append(cnt)
    for i in linkTeam:
        link += arr[cnt][i]
        link += arr[i][cnt]
    dfs(start,link+temp,cnt+1)
    linkTeam.pop()
    
    
dfs(0,0,0)
print(min(ans))
                
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
'''