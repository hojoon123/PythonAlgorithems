import sys
from collections import deque
input = sys.stdin.readline

a = deque()
b = deque()
n = int(input())
[a.append(_) for _ in list(map(int,input().split()))]

for i in range(n):
    j = i+1
    try:
        while a[i] > a[j]:
            j += 1
        else:
            b.append(a[j])
    except:
        b.append(-1)

print(*b)
'''
 Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
 없으면 -1이 오큰수
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)
수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)

총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력
예제 입력 1 
4
3 5 2 7
예제 출력 1 
5 7 7 -1
'''