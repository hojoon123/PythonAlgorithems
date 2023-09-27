import sys
from itertools import combinations
input = sys.stdin.readline

def func(depth,tmp):
    if depth == 3:
        if tmp <= n:
            result.append(tmp)
        return
    for i in range(m):
        if visited[i] == 0:
            visited[i] = 1
            func(depth+1,tmp+arr[i])
            visited[i] = 0

if __name__ == "__main__":
    result = []
    m , n = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * m
    func(0, 0)
    print(max(result))

'''
5 21
5 6 7 8 9

21
예제 입력 2 
10 500
93 181 245 214 315 36 185 138 216 295
예제 출력 2 
497
'''