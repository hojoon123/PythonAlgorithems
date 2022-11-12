import sys
from math import sqrt
input = sys.stdin.readline
def bubsort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-1-i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
bubsort(arr)
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