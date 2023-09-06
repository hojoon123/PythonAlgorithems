import sys
input = sys.stdin.readline


def dfs(cnt):
    if cnt == 81:
        for i in range(9):
            print(*board[i])
        quit()

    x = cnt // 9
    y = cnt % 9
    if board[x][y] == 0:
        for i in range(1, 10):
            if not col[x][i] and not row[y][i] and not rect[(x // 3) * 3 + (y // 3)][i]:
                col[x][i] = 1
                row[y][i] = 1
                rect[(x // 3) * 3 + (y // 3)][i] = 1
                board[x][y] = i
                dfs(cnt + 1)
                board[x][y] = 0
                rect[(x // 3) * 3 + (y // 3)][i] = 0
                row[y][i] = 0
                col[x][i] = 0
    else:
        dfs(cnt + 1)


if __name__ == '__main__':
    board = [[0 for _ in range(9)] for _ in range(9)]
    col = [[0 for _ in range(10)] for _ in range(9)]
    row = [[0 for _ in range(10)] for _ in range(9)]
    rect = [[0 for _ in range(10)] for _ in range(9)]

    for i in range(9):
        number = input().strip().split()
        for j in range(len(number)):
            board[i][j] = int(number[j])
            if board[i][j] != 0:
                col[i][board[i][j]] = 1
                row[j][board[i][j]] = 1
                rect[(i // 3) * 3 + (j // 3)][board[i][j]] = 1

    dfs(0)

'''
와 이거 진짜 잘 짠 코드다
기존의 코드는 계속해서 처음부터 보드를 탐색했다면, 이 코드는
처음에 col row rect를 생성해서 값을 1로 집어넣어버림
그 후, not으로 해당 좌표에 있는지만 체크하고 넘어가니까 시간을 압도적으로 줄일 수 있음.
'''