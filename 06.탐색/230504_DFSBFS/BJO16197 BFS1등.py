import sys

input = lambda: sys.stdin.readline().rstrip()


def get():
    if len(q) == 0:
        return False
    else:
        val = q.pop(0)
        return val


def bfs(a1, b1, a2, b2):
    q.clear()
    q.append([a1, b1, a2, b2])
    visited = [[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[a1][b1][a2][b2] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        a1, b1, a2, b2 = get()
        if visited[a1][b1][a2][b2] >= 10:
            break
        for i in range(4):
            na1 = a1 + dx[i]
            nb1 = b1 + dy[i]
            na2 = a2 + dx[i]
            nb2 = b2 + dy[i]

            if not (0 <= na1 < n and 0 <= nb1 < m) and not (0 <= na2 < n and 0 <= nb2 < m):
                continue
            if not (0 <= na1 < n and 0 <= nb1 < m):
                return visited[a1][b1][a2][b2] + 1
            if not (0 <= na2 < n and 0 <= nb2 < m):
                return visited[a1][b1][a2][b2] + 1
            if graph[na1][nb1] == "#":
                na1, nb1 = a1, b1
            if graph[na2][nb2] == "#":
                na2, nb2 = a2, b2

            if visited[na1][nb1][na2][nb2] == -1:
                visited[na1][nb1][na2][nb2] = visited[a1][b1][a2][b2] + 1
                q.append([na1, nb1, na2, nb2])
    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    q = []
    x1, y1, x2, y2 = 0, 0, 0, 0
    cng = True
    for i in range(n):
        graph.append(list(input()))
        for j in range(m):
            if graph[i][j] == "o":
                if cng:
                    x1, y1 = i, j
                    cng = False
                else:
                    x2, y2 = i, j

    print(bfs(x1, y1, x2, y2))