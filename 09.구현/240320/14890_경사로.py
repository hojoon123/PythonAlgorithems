import sys
input = sys.stdin.readline

def check(line, l):
    visited = [False for _ in range(n)]
    
    for i in range(n-1):
        if line[i] == line[i+1]:
            continue

        elif abs(line[i] - line[i+1]) > 1:
            return False
        
        # 내리막길
        elif line[i] > line[i+1]:
            n_node = line[i+1]
            for j in range(i+1, i+l+1):
                if 0 <= j < n:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if n_node != line[j]:
                        return False

                    elif visited[j]:
                        return False

                    visited[j] = True
                else:
                    return False
        
        # 오르막길
        else:
            n_node = line[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if n_node != line[j]:
                        return False
                    
                    elif visited[j]:
                        return False
                    
                    visited[j] = True
                else:
                    return False
    return True

if __name__ == "__main__":
    n, l = map(int, sys.stdin.readline().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n):
        # 가로 체크
        if check(graph[i], l):
            ans += 1
            
        # 세로 체크
        tmp = [graph[j][i] for j in range(n)]
        if check(tmp, l):
            ans += 1

    print(ans)