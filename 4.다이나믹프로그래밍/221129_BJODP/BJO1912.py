import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for i in range(N-1):
    dp.append(max(dp[i]+arr[i+1],arr[i+1]))
print(max(dp))
'''
연속합 
연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
33
'''