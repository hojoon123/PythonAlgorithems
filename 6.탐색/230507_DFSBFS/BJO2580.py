import sys
input = sys.stdin.readline


# x 세로줄의 n이 있는지 확인
def checkRow(r, n):
    for i in range(9):
        if n == graph[r][i]:
            return False
    return True


# y 가로줄의 n이 있는지 확인
def checkCol(c, n):
    for i in range(9):
        if n == graph[i][c]:
            return False
    return True


# x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
def checkRect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True


# dfs + 백트래킹
def solution(n):
    if n == len(blank):
        for k in range(9):
            print(*graph[k])
        exit(0)

    for i in range(1, 10):
        x = blank[n][0] # 빈칸의 x좌표
        y = blank[n][1] # 빈칸의 y좌표

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            solution(n + 1)
            graph[x][y] = 0

if __name__ == '__main__':
    graph = []
    blank = []
    for i in range(9):
        graph.append(list(map(int, input().split())))
        for j in range(9):
            if graph[i][j] == 0:
                blank.append([i, j])

    solution(0)
'''
0이 빈칸이니까 빈칸들 먼저 찾아서 idx 저장해두기
탐색해서 하나씩 리스트에 넣고 숫자 넣고 중복 제거 이후
1부터 9까지 리스트에서 중복제거한 숫자들 빼기
1개만 남았다면 바로 숫자 넣기
남은게 넣을 수 있는 숫자들이니까
하나씩 집어넣고 다음 꺼 진행하기

넣을 수 있는 숫자가 없으면 리턴



아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판
스도쿠 판의 빈 칸의 경우에는 0

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력

예제 입력 1 
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
예제 출력 1 
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''