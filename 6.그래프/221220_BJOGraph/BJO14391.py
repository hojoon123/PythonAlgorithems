from sys import stdin
input = stdin.readline


N, M = map(int,input().split())
arr = []
[arr.append(list(map(int,input().rstrip()))) for i in range(N)]
ans = []
for i in range(1 << N * M): # 0000 0001을 6만큼 이동한 값 0100 0000 즉 64회 반복
    total = 0 # 합 초기화
    #가로합 계산
    for row in range(N):
        rowsum = 0
        for col in range(M):
            # idx는 2차원 행렬을 1줄로 만들었을때의 인덱스
            idx = row * M + col
            if i & (1 << idx) != 0: #i 와 1<<idx의 공집합이 0이 아니면 기존 값 10배 + 새 값
                rowsum = rowsum * 10 + arr[row][col]
            else:# 0이라면 지금까지의 값을 더함
                total += rowsum
                rowsum = 0
        total += rowsum


    #세로합 계산
    for col in range(M):
        colsum = 0
        for row in range(N):
            idx = row * M + col
            if i & (1 << idx) == 0: #(0이면 세로로 더한다)
                colsum = colsum * 10 + arr[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)
print(max(ans))
'''
크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 4)
열 행 순으로 주어짐
0부터 9까지 중 하나
예제 입력 1 
2 3
123
312
예제 출력 1 
435
'''