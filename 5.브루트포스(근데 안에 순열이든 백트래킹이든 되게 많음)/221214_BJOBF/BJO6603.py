import sys
from itertools import permutations
input = sys.stdin.readline

def dfs():
    if len(arr)== 6:
        print(*arr)
        return
    
    for i in range(N[0]):
        
        if len(arr) == 0:
            arr.append(N[i+1])
            visited[i] = 1
            dfs()
            arr.pop()
            visited[i] = 0
            
        else:
            if not visited[i] and N[i+1] > arr[-1] :
                arr.append(N[i+1])
                visited[i] = 1
                dfs()
                arr.pop()
                visited[i] = 0
while 1:
    N = list(map(int,input().split())) # N[0] k (6 < k < 13) S N[1:] sort 돼서 들어옴
    visited = [0] * N[0]
    arr = []
    if N[0] == 0:
        exit()
    dfs()
    print()

            
'''
예제 입력 1 
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
예제 출력 1 
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
'''