import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
if n <= 3: print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)
'''
순서 상관 x 겹침 x
첫째 줄에 2 * n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력
예제 입력 1 
2
9
예제 출력 1 
2
55
'''