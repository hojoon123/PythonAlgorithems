N = int(input()) #하향식 코드
cache = {1: 0, 2: 1}

def dp(n):
    if n in cache:
        return cache[n]
    # 핵심 코드
    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    cache[n] = cnt
    return cnt
    
print(dp(N))

'''
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N 
첫째 줄에 연산을 하는 횟수의 최솟값을 출력
예제 입력 1 
2
10
예제 출력 1 
1
3
'''