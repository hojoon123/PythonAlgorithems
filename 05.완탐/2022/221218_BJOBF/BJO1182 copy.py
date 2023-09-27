import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    combi = combinations(arr, i)

    for x in combi:
        if sum(x) == S:
            cnt += 1

print(cnt)



'''
(1 ≤ N ≤ 20, |S| ≤ 1,000,000)

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
'''