import sys

input = sys.stdin.readline
def mersort(l):
  if len(l) <= 1: return  # 정렬할 리스트 개수가 1개 이하면 정렬 필요 x
  
  # 그룹을 나눠 각각 병합 정렬 호출
  mid = len(l) // 2  # 중간을 기준으로 두 그룹으로 나누기
  g1 = l[:mid]  
  g2 = l[mid:] 
  mersort(g1)
  mersort(g2)
  
  # 두 그룹 병합
  i1 = 0  # 1번 그룹 인덱스
  i2 = 0  # 2번 그룹 인덱스
  il = 0  # 함수에 주어진 리스트 인덱스

  while i1 < len(g1) and i2 < len(g2):
    if g1[i1] < g2[i2]: # 만약 1번 그룹의 i1 인덱스 실값이 2번 그룹의 i2 인덱스 실값보다 작다면
      l[il] = g1[i1]  # 리스트에는 g1[i1] 값이 먼저 담김
      i1 += 1 # 다음 진행을 위해 인덱스 수 + 1
    else:
      l[il] = g2[i2]
      i2 += 1
    il += 1

  # while 루프 후 남아 있는 자료들을 결과에 추가
  while i1 < len(g1):
    l[il] = g1[i1]
    i1 += 1
    il += 1
  while i2 < len(g2):
    l[il] = g2[i2]
    i2 += 1
    il += 1

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
mersort(arr)
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