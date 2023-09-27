import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int,input().split())
numbers = sorted(map(int, input().split()))
arr = []
def dfs():
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(N):
        arr.append(numbers[i])
        dfs()
        arr.pop()
        
dfs()
'''
예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5
'''