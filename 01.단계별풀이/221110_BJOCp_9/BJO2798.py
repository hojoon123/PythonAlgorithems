import sys
from itertools import combinations
input = sys.stdin.readline
m , n = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = []

for i in combinations(arr, 3):
    if(sum(i)) <= n:
        result.append(sum(i))
    else:
        pass
print(max(result))

'''
5 21
5 6 7 8 9

21
'''