import sys
input=sys.stdin.readline

N, M = map(int,input().split())
li = sorted(map(str,input().split()))
arr = []
visited = [0] * M
vowel = ['a','e','i','o','u']
def dfs():
  vowel_cnt = 0
  consonant_cnt = 0
  if len(arr) == N:
    
    for i in range(N):
      if arr[i] in vowel:
        vowel_cnt += 1
      else:
        consonant_cnt += 1
        
    if vowel_cnt >= 1 and consonant_cnt >= 2:
      print(''.join(arr))
      
    return
  
  for i in range(M):
    if len(arr) == 0:
      arr.append(li[i])
      visited[i] = 1
      dfs()
      arr.pop()
      visited[i] = 0
        
    else:
      if not visited[i] and ord(li[i]) > ord(arr[-1]):
        arr.append(li[i])
        visited[i] = 1
        dfs()
        arr.pop()
        visited[i] = 0

dfs()

'''
최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
예제 입력 1 
4 6
a t c i s w
예제 출력 1 
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''