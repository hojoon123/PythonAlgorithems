import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
res = list(combinations(arr,M))
[print(*res[i]) for i in range(len(res))]

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