import sys
input = sys.stdin.readline

def dfs(idx, sub_sum):
    global cnt
    if idx >= N:
        return
    sub_sum += arr[idx]
    if sub_sum == S:
        cnt += 1
        
    dfs(idx+1, sub_sum)
    dfs(idx+1, sub_sum - arr[idx])

N, S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
dfs(0,0)
print(cnt)



'''
(1 ≤ N ≤ 20, |S| ≤ 1,000,000)

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
'''