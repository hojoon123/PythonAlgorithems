import sys

input = sys.stdin.readline
def cntsort(arr):
  count = [0] * (max(arr) + 1)

  for num in arr:
      count[num] += 1
      
  for i in range(1, len(count)):
      count[i] += count[i-1]

  result = [0] * (len(arr))

  for num in arr:
      idx = count[num]
      result[idx - 1] = num
      count[num] -= 1
  
  return result    

n = int(input())
arr = []

for i in range(n):
  arr.append(int(input()))
  
for j in cntsort(arr):
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