import sys
from math import sqrt
input = sys.stdin.readline
def solution(l, start, end):
    # 정렬 대상이 1개 이하이면 종료
    if end - start <= 0: return

    pivot = l[end] # 기준값을 정함
    i = start
    for j in range(start, end):
        if l[j] <= pivot:	# 피벗값보다 j 값이 작거나 같다면
            l[i], l[j] = l[j], l[i]	# i와 j 실제 값을 바꿔줌
            i += 1	# i 인덱스는 한 칸 뒤로
    l[i], l[end] = l[end], l[i]

    # 재귀 호출
    solution(l, start, i - 1)   # 기준 값보다 작은 그룹을 재귀 호출로 정렬
    solution(l, i + 1, end) # 기준 값보다 큰 그룹을 재귀 호출로 정렬


def quick_sort(l):
    solution(l, 0, len(l)-1)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
quick_sort(arr)
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