import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(2)]
    for i in range(1,N):
        if i == 1:
            arr[0][1] += arr[1][0]
            arr[1][1] += arr[0][0]
        else:
            arr[0][i] += max(arr[1][i-1],arr[1][i-2])
            arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    print(max(arr[0][N-1],arr[1][N-1]))
'''
2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력
예제 입력 1 
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
예제 출력 1 
260
290
'''