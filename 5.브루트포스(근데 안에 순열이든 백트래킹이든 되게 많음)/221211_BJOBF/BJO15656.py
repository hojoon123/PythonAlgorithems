import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combi(arr[:], n - 1):
            result.append([elem] + rest)
    return result
res = list(combi(arr,M))
[print(*res[i]) for i in range(len(res))]
'''
예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5
'''