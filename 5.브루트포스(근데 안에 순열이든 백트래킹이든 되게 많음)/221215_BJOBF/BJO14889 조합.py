import sys
from itertools import combinations
from itertools import permutations
input = sys.stdin.readline
#그냥 생각나는 대로 품
# 백트래킹랑 재귀 쓰기 싫어서 라이브러리 활용해가지고 했는데
# 대충 봐도 이건 아니다싶을 정도의 반복ㅋㅋ 근데 20 이하라 아슬아슬 통과띠;;
# 3584 ㄷㄷ 근데 백트래킹으로도 해보니 시간 똑같네 어차피 다 돌려야 해서 오래 걸리는 건 같군
N = int(input())
N_lis = [i for i in range(1,N+1)]
cost = list(combinations(N_lis,N//2))
idx = len(cost)
cost_value = [0] * idx
res = []
arr = [list(map(int,input().split())) for i in range(N)]

for i in range(idx):
    value = 0
    tmp = list(permutations(cost[i],2))
    for j,k in tmp:
        value += arr[j-1][k-1]
    cost_value[i] = value
        
for i in range(idx//2):
    res.append(abs(cost_value[i] - cost_value[idx-i-1]))
print(min(res))
                
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