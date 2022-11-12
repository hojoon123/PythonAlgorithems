import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
    
a.sort()

cnt = Counter(a).most_common()

try:
    if cnt[0][1] == cnt[1][1]:
        mode = cnt[1][0]
    else:
        mode = cnt[0][0]
except:
    mode = cnt[0][0]

print(round(sum(a)/n))
print(a[n//2])
print(mode)
print(max(a)-min(a))
    
'''''
첫 줄 n개 N은 홀수
둘 줄부터 n개 
-4000 < a < 4000
정렬 
 산술평균 첫째 자리에서 반올림한 값 sum(a) / n {0:.1f}
 중앙값 a[n // 2] 홀수로 주어졌기 때문에 그냥 중앙값만
 최빈값 여러 개 있을 때 최빈값 중 두 번째로 작은 값 카운팅정렬쓰는게좋을듯
 범위 max(a) - min(a)
예제 입력 1 
5
1
3
8
-2
2
예제 출력 1 
2
2
1
10
'''