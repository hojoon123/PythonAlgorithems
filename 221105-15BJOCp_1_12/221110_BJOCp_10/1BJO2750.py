import sys
from math import sqrt
input = sys.stdin.readline
def inssort(l):
  for i in range(1, len(l)):  # 1부터 n까지 i
    key = l[i]  # 일단 key는 l[i]의 값. 아직 정렬이 안 된 정렬해야 하는 값임
    # 인덱스가 아니라 아예 데이터를 저장하는 방식
    j = i - 1 # j는 i보다 1 작은 인덱스로 시작
    
    while j >= 0 and l[j] > key:  # j가 0보다 크고, j 안의 값이 key보다 크다면
      l[j+1] = l[j] # 앞의 값을 뒤로 복사한다(덮어씀)
      j -= 1  # 그리고 j는 앞으로 한 칸 옮김
    
    l[j+1] = key  # while 루프에서 탈출하면, 루프 1회마다 l[j+1]에 현재 key를 복사함. 
    # 이제 찾은 위치에 정렬 대상인 key를 삽입한다

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
inssort(arr)
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