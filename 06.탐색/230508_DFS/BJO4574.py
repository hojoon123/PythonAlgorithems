import sys
input = sys.stdin.readline


def dfs(cnt, num):
    flag = False
    
    if cnt == d_cnt:
        print('Puzzle', num)
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        return True

    x,y = domino[cnt]
    if board[x][y]:
        flag = dfs(cnt + 1, num)
        return flag
    
    for i in range(9):
        for j in range(9):
            if i == j or visited[i][j]:
                continue
            for d in dxdy:
                swap_x, swap_y = x + d[0], y + d[1]
                if 0 <= swap_x <= 8 and 0 <= swap_y <= 8 and not board[swap_x][swap_y]:
                    if row[x][i] == row[swap_x][j] == col[y][i] == col[swap_y][j] == rect[x // 3 * 3 + y // 3][i] == rect[swap_x // 3 * 3 + swap_y // 3][j] == 0:
                        col[y][i], col[swap_y][j] = 1, 1
                        row[x][i], row[swap_x][j] = 1, 1
                        rect[x // 3 * 3 + y // 3][i], rect[swap_x // 3 * 3 + swap_y // 3][j] = 1, 1
                        board[x][y], board[swap_x][swap_y] = i + 1, j + 1
                        visited[i][j], visited[j][i] = 1, 1
                        flag = dfs(cnt + 1, num)
                        if flag:
                            return flag
                        
                        board[x][y], board[swap_x][swap_y] = 0, 0
                        col[y][i], col[swap_y][j] = 0, 0
                        row[x][i], row[swap_x][j] = 0, 0
                        rect[x // 3 * 3 + y // 3][i], rect[swap_x // 3 * 3 + swap_y // 3][j] = 0, 0
                        visited[i][j], visited[j][i] = 0, 0
    return flag


if __name__ == '__main__':
    lc = ['A','B','C','D','E','F','G','H','I']
    puzNum = 1
    dxdy = [[0, 1], [1, 0]]
    while 1:
        m = int(input())
        if m == 0:
            break
        board = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        row = [[0] * 9 for _ in range(9)]
        rect = [[0] * 9 for _ in range(9)]
        visited = [[0] * 9 for _ in range(9)]
        domino = []
        d_cnt = 0
        for i in range(m):
            n1, ln1, n2, ln2 = input().strip().split()
            n1, n2 = int(n1), int(n2)
            lcTmpR1, lcTmpC1 = lc.index(ln1[0]), int(ln1[1]) - 1
            lcTmpR2, lcTmpC2 = lc.index(ln2[0]), int(ln2[1]) - 1
            board[lcTmpR1][lcTmpC1] = n1
            board[lcTmpR2][lcTmpC2] = n2
            row[lcTmpR1][n1-1], row[lcTmpR2][n2-1] = 1, 1
            col[lcTmpC1][n1-1], col[lcTmpC2][n2-1] = 1, 1
            rect[(lcTmpR1 // 3) * 3 + (lcTmpC1 // 3)][n1-1] = 1
            rect[(lcTmpR2 // 3) * 3 + (lcTmpC2 // 3)][n2-1] = 1
            
        numsLocation = input().strip().split()
        for j in range(len(numsLocation)):
            r, c = lc.index(numsLocation[j][0]), int(numsLocation[j][1]) - 1
            board[r][c] = j + 1
            row[r][j] = 1
            col[c][j] = 1
            rect[(r // 3) * 3 + (c // 3)][j] = 1
            
        for i in range(9):
            for j in range(9):
                if not board[i][j]:
                    domino.append([i, j])
                    d_cnt += 1
                    
        dfs(0, puzNum)
        puzNum += 1

'''
스도미노쿠 WHILE 1 로 해서 0 이면 종료하기
n 입력받고 n줄 만큼 2개씩 묶어논 도미노 타일 입력
행 1~9
열 A~I
마지막 줄 1~9값을 좌표인덱스에 넣음.

처음에 자기 수 빼고 묶음으로 72개 만들어놓고 거기서 입력받을 때 마다
값 빼고 입력받은 값을 자리에 넣는 식으로 진행
남은 묶음은 리스트 형태 [1,3] 서로 자리도 바꿔보면서 맞춰야함 1번했다가 3번했다가
방식은 그 전이랑 동일하게 해도 될 듯.
의외로 할만 할지도

예제 입력 1 
10
6 B2 1 B3
2 C4 9 C3
6 D3 8 E3
7 E1 4 F1
8 B7 4 B8
3 F5 2 F6
7 F7 6 F8
5 G4 9 G5
7 I8 8 I9
7 C9 2 B9
C5 A3 D9 I4 A9 E5 A2 C6 I1
11
5 I9 2 H9
6 A5 7 A6
4 B8 6 C8
3 B5 8 B4
3 C3 2 D3
9 D2 8 E2
3 G2 5 H2
1 A2 8 A1
1 H8 3 I8
8 I3 7 I4
4 I6 9 I7
I5 E6 D1 F2 B3 G9 H7 C9 E5
0
예제 출력 1 
Puzzle 1
872643195
361975842
549218637
126754983
738169254
495832761
284597316
657381429
913426578
Puzzle 2
814267593
965831247
273945168
392176854
586492371
741358629
137529486
459683712
628714935
'''