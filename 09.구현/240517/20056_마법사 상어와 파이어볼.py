import sys
from collections import deque
input = sys.stdin.readline

def magic(graph, fire_balls, n, k):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    for _ in range(k):
        while fire_balls:
            r, c, v, s, d = fire_balls.popleft()
            nr = (r + s * dx[d]) % n
            nc = (c + s * dy[d]) % n
            graph[nr][nc].append([v,s,d])
            
        for i in range(n):
            for j in range(n):
                if len(graph[i][j]) > 1: # 한 곳에 두개 이상
                    sum_v, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[i][j])
                    while graph[i][j]:
                        cv, cs, cd = graph[i][j].pop()
                        sum_v += cv
                        sum_s += cs
                        if cd % 2:
                            cnt_odd += 1
                        else:
                            cnt_even += 1
                    if cnt_odd == cnt or cnt_even == cnt:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]

                    if sum_v // 5:
                        for d in nd:
                            fire_balls.append([i, j, sum_v//5, sum_s//cnt, d])
                
                if len(graph[i][j]) == 1:
                    fire_balls.append([i,j] + graph[i][j].pop())
    
    ans = sum(f[2] for f in fire_balls)
    return ans
    
def main():
    n, m, k = map(int,input().split())
    graph = [[[] for i in range(n)] for j in range(n)]
    fire_balls = deque()
    for i in range(m):
        r, c, v, s, d = map(int,input().split())
        fire_balls.append([r-1,c-1,v,s,d])
        
    print(magic(graph, fire_balls, n, k))
        
if __name__ == "__main__":
    main()
    