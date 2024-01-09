from collections import deque
n = int(input())
visit = []
shark = [0,0]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(n):
    cur= list(map(int, input().split()))
    for j,num in enumerate(cur):
        if num == 9:
            shark = [i,j]
    visit.append(cur)


def findway(ssize, visit, loc):
    qu = deque()
    min_dist = float('inf')
    qu.append((loc, 0))
    ret_list = []
    visited = [[False] * n for _ in range(n)]
    while qu:
        shark_pos, cur_dist = qu.popleft()
        sy,sx = shark_pos
        if cur_dist > min_dist:
            break
        if visit[sy][sx] < ssize:
            if visit[sy][sx] == 0:
                for dy, dx in dirs:
                    ny, nx = dy+sy, dx+sx
                    if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                        qu.append(([ny,nx], cur_dist +1))
                        visited[ny][nx] = True
            else:
                ret_list.append((sy,sx))
                min_dist = cur_dist
                continue
        elif visit[sy][sx] == ssize or visit[sy][sx] == 9:
            if visit[sy][sx] == 9:
                visit[sy][sx] =0
            for dy, dx in dirs:
                ny, nx = dy + sy, dx + sx
                if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                    qu.append(([ny,nx],cur_dist+1))
                    visited[ny][nx] = True
        else:
            continue

    ret_list.sort(key=lambda x: (x[0],x[1]))
    if not ret_list:
        return 0,0
    return ret_list[0], min_dist

ret =0
ssize =2
cur_eat = 0
while True:
    next_shark, add = findway(ssize, visit, shark)
    if add ==0:
        break
    else:
        ret +=add
        shark = next_shark
        sy, sx = next_shark
        visit[sy][sx] = 0
        cur_eat +=1
        if cur_eat == ssize:
            ssize +=1
            cur_eat =0

print(ret)