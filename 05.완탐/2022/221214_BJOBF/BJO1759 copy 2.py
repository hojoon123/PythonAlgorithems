import sys
input=sys.stdin.readline

def dfs(start):
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
  
  for i in range(start,M):
    arr.append(li[i])
    dfs(i + 1)
    arr.pop()
    
N, M = map(int,input().split())
li = sorted(map(str,input().split()))
arr = []
vowel = ['a','e','i','o','u']
dfs(0)
# 제일 첫번째 시도보다 3배 빠름 3배 덜 돌음
# 다 돌면서 ord 변환해서 체크하고 넘기는 것 보다 애초에 for문 돌아가는 수를
# 줄여서 시간적인 이득을 봄
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