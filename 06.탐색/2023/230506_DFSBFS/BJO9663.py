import sys
input = sys.stdin.readline


def appoint(idx):
    global ans

    if idx == n:
        ans += 1
        return

    for i in range(n):
        board[idx] = i
        for x in range(idx):
            if board[idx] == board[x] or abs(board[idx] - board[x]) == idx - x:
                break
        else:
            appoint(idx + 1)

if __name__ == '__main__':
    n = int(input())
    board = [0] * n
    ans = 0
    appoint(0)
    print(ans)


'''
8개 먼저 다 뿌리고 
if 현재 내 8방위에 걸리는 애가 있는가? 없으면 다음애로 체크 체크 체크 8개 다 하고도 멀쩡하면 리턴 + 1

먼저 퀸을 백트래킹을 사용해서 배치
이후 dfs를 이용해서 탐색
예제 입력 1 
8
예제 출력 1 
92
'''