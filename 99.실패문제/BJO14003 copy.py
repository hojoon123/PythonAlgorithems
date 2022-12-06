import sys
import bisect
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for i in range(N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else: #dp가 정렬되어있을 경우 arr[i]의 인덱스 반환
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]        
print(len(dp))

max_dp = len(dp)
lis = []

for i in range(N, 0, -1):
    if arr[i] == max_dp:
        lis.append(arr[i])
        max_dp -= 1


lis.reverse()
print(*lis)

'''
예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4

'''