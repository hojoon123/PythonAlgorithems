import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
perm = list(permutations(arr,N))
result = -1000

def cal(li):
    sum_arr = 0
    for i in range(len(li)-1):
        sum_arr += abs(li[i] - li[i+1])
    return sum_arr

for j in perm:
    result = max(result,cal(j))
print(result)
'''
0보다 큰 애랑 작은 애를 한 쌍으로 묶어서 빼두고 나머지 애들 중에서
제일 큰 수 랑 제일 작은 수끼리 쌍 만들어주기
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
-100보다 크거나 같고, 100보다 작거나 같다
예제 입력 1 
6
20 1 15 8 4 10
예제 출력 1 
62
'''