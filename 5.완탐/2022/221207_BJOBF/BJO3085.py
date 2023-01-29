import sys
from math import sqrt
input = sys.stdin.readline

def Check(arr):
    N = len(arr)
    answer = 0
    
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
                
        cnt = 1
        for j in range(1,N):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer

N = int(input())
arr = [list(str(input().rstrip())) for i in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N: #끝 제외
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            tmp = Check(arr)
            
            if tmp > answer:
                answer = tmp

            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i + 1 < N: #끝 제외
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            tmp = Check(arr)
            
            if tmp > answer:
                answer = tmp

            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(answer)
'''
예제 입력 1 
3
CCP
CCP
PPC
예제 출력 1 
3
'''