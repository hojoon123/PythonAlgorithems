import sys
from itertools import combinations
input = sys.stdin.readline
m , n = map(int,input().split())
arr = list(map(int,input().split()))

result = []

for i in combinations(arr, 3):
    if(sum(i)) <= n:
        result.append(sum(i))
    else:
        pass
print(max(result))

'''
카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)
 둘째 줄에는 카드에 쓰여 있는 수 0 < a < 100000
 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
    
예제 입력 1 
5 21
5 6 7 8 9
예제 출력 1 
21
'''