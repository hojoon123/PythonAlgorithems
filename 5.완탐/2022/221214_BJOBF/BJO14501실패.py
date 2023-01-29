import sys
input=sys.stdin.readline

N = int(input())
TP = [list(map(int,input().split())) for i in range(N)]
dp = [TP[0][1]]
tmp = TP[0][0]
tmp2 = 0
for i in range(1,N+1):
  try:
    if tmp + TP[tmp][0] <= N:
      if TP[i][1] > dp[i-1] + TP[tmp][1]:
        dp.append(TP[i][1])
        tmp = TP[i][0]
        
      else:
        for j in range(tmp,N+1):
          if tmp + TP[j][0] <= N:
            dp.append(max(dp[i-1] + TP[tmp][1],dp[i-1] + TP[j]))
            if TP[j] > TP[tmp][1]:
              tmp2 = j
        tmp = tmp + TP[tmp2][0]
  except:
    pass
print(dp)
print(max(dp))
#for 문을 2중으로 중첩해서 가성비도 딸림 이럴거면 걍 브루트포스로 해도 됐음.
#첨엔 1번만 써서 돌렸는데, 30을 물어야 하는데 20을 물음 특정 상황에서 제대로 발동하지 않음
#점화식은 제대로 캐치함. 문제해결능력은 괜찮았음. 그런데 구현에서 문제가 발생
#DP를 제대로 이해하지 못하고 풀었다는 뜻임 솔루션 확인 후 이해하고 넘어감
'''
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