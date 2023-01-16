import sys
#어떻게 이런 코드를 생각했을까
#보고도 완벽히 이해하기 난해해따...
#대충은 이해했다. 1400ms 코드의 큰 틀은 같으니, 그러나 중요한 건 해당 코드는
#무려 10배나 적은 140ms의 시간이 나왔다. 
#솔직히 이 방식으로 다시 풀라고 해도 못 풀 것 같다. 공부를 더 하고 나중에 다시 돌이켜보자
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def check(bit):
    total = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    # 가로
    for r, x in enumerate(bit):
        i = 0
        while i < M:
            if (x >> i) & 1 == 0:
                j = i + 1
                while j < M and (x >> j) & 1 == 0:
                    j += 1
                val = []
                for k in range(i, j + 1):
                    visited[r][M - 1 - k] = True
                    val.append(board[r][M - 1 - k])
                val = list(reversed(val))
                total += int(''.join(val))
                i = j
            i += 1
    # 세로
    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                continue
            val = [board[r][c]]
            visited[r][c] = True
            for nr in range(r + 1, N):
                if visited[nr][c]:
                    break
                visited[nr][c] = True
                val.append(board[nr][c])
            total += int(''.join(val))

    return total

def dfs(bit, answer):
    if len(bit) < N:
        for x in range(2 ** (M - 1), 2 ** M):
            bit.append(x)
            dfs(bit, answer)
            bit.pop()
    else:
        result = check(bit)
        answer[0] = max(answer[0], result)

answer = [0]
dfs([], answer)
print(answer[0])
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