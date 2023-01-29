import sys
input=sys.stdin.readline

N = int(input())
T,P,dp = [],[],[]
for i in range(N):
  a,b = map(int,input().split())
  T.append(a)
  P.append(b)
  dp.append(b)
dp.append(0)# 끝부터 접근함. 나도 이렇게 유연한 사고가 가능해야 할텐데
for i in range(N - 1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
print(dp[0])

'''
      dp.append(dp[i-1] + TP[tmp][1])
      tmp = tmp + TP[tmp][0]

20 이 아니라 30을 물어야 됨 
N (1 ≤ N ≤ 15)
예제 입력 1 
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
예제 출력
90
'''