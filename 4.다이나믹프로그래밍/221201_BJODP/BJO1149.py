import sys
input = sys.stdin.readline
N = int(input())
RGB = []
for i in range(N): RGB.append(list(map(int,input().split())))
for i in range(1,N):
    RGB[i][0] = min(RGB[i-1][1],RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0],RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][1],RGB[i-1][0]) + RGB[i][2]
print(min(RGB[N-1][0],RGB[N-1][1],RGB[N-1][2]))
'''
N(2 ≤ N ≤ 1,000)
빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩
1 <= cell <= 1000
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력
예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
'''