N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])

'''

N은 이제 buy 보다 적게 남음 buy 보다 작은 인덱스의 수 중에서 가성비 다시 찾아
걍 첨부터 가성비 순위를 다 적어서 인덱스에 넣고 해당 순위대로 사면 될 듯
 카드의 개수 N
  P1부터 PN
  N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력
예제 입력 1 
4
1 5 6 7
예제 출력 1 
10
'''