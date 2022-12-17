import sys
from itertools import combinations
input=sys.stdin.readline

N, M = map(int,input().split())
li = sorted(map(str,input().split()))
vowel = ['a','e','i','o','u']
for i in combinations(li,N): 
  vowel_cnt = 0
  consonant_cnt = 0
  for j in i:
    if j in vowel: vowel_cnt += 1
    else: consonant_cnt += 1
    
  if vowel_cnt >= 1 and consonant_cnt >= 2:
    print(''.join(i))
#콤비쓴게 젤 빠름 ㅋㅋ 걍 콤비랑 펌 써도 되는 각이면 쓰는게 나음
#물론 반복문에서 컷 내는게 빠른 경우가 있으니 그 때 그 때 다름 이 경우에는
#어차피 len(arr)에서 덜어내주는 경우라 콤비 쓰나 재귀 때리나 똑같음
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