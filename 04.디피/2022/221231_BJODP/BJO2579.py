from sys import stdin
input = stdin.readline

N = int(input())
arr = [0] * (N + 1) #걍 301로 해놓고 하면 되게 편한데 메모리를 그래도 최소화 하고 싶었음
dp = [0] * (N + 1)

for i in range(N):
    arr[i] = int(input())

dp[0] = arr[0]

try:
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1] + arr[2], arr[0] + arr[2])
    
    for i in range(3,N):
        if dp[i-2] + arr[i] > dp[i-3] + arr[i] + arr[i-1] : # 0 23 01 3 비교
            dp[i] = dp[i-2] + arr[i]
        else:
            dp[i] = dp[i-3] + arr[i] + arr[i-1]
except:
    pass

print(dp[N - 1])
    

'''
연속 3개 x 
다음 다다
계단의 개수
N 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수
예제 입력 1 
6
10
20
15
25
10
20
예제 출력 1 
75
'''