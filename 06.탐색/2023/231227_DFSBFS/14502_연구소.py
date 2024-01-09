from sys import stdin
from itertools import combinations
input = stdin.readline

# 그래프, n과m, 빈 공간, 바이러스, 벽이 아닌 칸의 수
def solve(world, n, m, blanks, virus, not_wall):

    ans = 0 
    for build in combinations(blanks, 3):
        # 1차원 배열이기에 슬라이싱을 사용한 얕은 복사가 가능
        q = virus[:]
        infection = 0 # 바이러스 수
        tmp_world = world[:]
        for pos in build:
            tmp_world[pos] = 1
            
        while q:
            idx = q.pop()
            infection += 1
            r, c = idx // m, idx % m
            
            # 상하좌우 돌리기 -1이면 인덱스 벗어남
            adj = [
                idx - m if 0 < r else -1,
                idx + m if r < n - 1 else -1,
                idx - 1 if 0 < c else -1,
                idx + 1 if c < m - 1 else -1
            ]
            
            for nxt in adj:
                if nxt != -1 and tmp_world[nxt] == 0:
                    tmp_world[nxt] = 2
                    q.append(nxt)

        # 벽을 제외한 수 - 바이러스 수
        cur = not_wall - infection
        if ans < cur:
            ans = cur

    return ans

def main():
    n, m = map(int, input().split())
    length = n * m
    world = [0] * length
    for i in range(0, length, m): # 1차원 배열
        world[i:i + m] = [*map(int, input().split())]
    
    blanks = []
    virus = []
    for i in range(length):
        if world[i] == 0:
            blanks.append(i)
        elif world[i] == 2:
            virus.append(i)
    not_wall = len(blanks) + len(virus) - 3
    
    print(solve(world, n, m, blanks, virus, not_wall))
    

if __name__ == '__main__':
    main()