import sys
from math import sqrt
input = sys.stdin.readline
def selsort(n):
    for i in range(len(n)-1):
        min_idx = i
        for j in range(i+1, len(n)): 
            if n[min_idx] > n[j]:
                min_idx = j 
        n[i], n[min_idx] = n[min_idx], n[i]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
selsort(arr)
for j in arr:
    print(j)
    
''''
첫째 줄에 수의 개수 N
둘째 줄부터 N개의 줄에는 수
-1000 <= n <= 1000
예제 입력 1 
5
5
2
3
4
1
예제 출력 1 
1
2
3
4
5
'''