from sys import stdin
from itertools import combinations
input = stdin.readline
def solve():
    N, M = map(int, input().split())
    length = N * M
    world = [0] * length
    for i in range(0, length, M): # 1차원 배열
        world[i:i + M] = [*map(int, input().split())]

    blanks = []
    virus = []
    for i in range(length):
        if world[i] == 0:
            blanks.append(i)
        elif world[i] == 2:
            virus.append(i)

    not_wall = len(blanks) + len(virus) - 3
    ans = 0 
    for build in combinations(blanks, 3):
        que = virus[:]
        tmp_world = world[:]
        infection = 0
        for pos in build:
            tmp_world[pos] = 1
        while que:
            idx = que.pop()
            infection += 1
            r, c = idx // M, idx % M
            adj = [
                idx - M if 0 < r else -1, #첫 줄이 아니면
                idx + M if r < N - 1 else -1, #마지막 줄이 아니면
                idx - 1 if 0 < c else -1, #첫번째가 아니면
                idx + 1 if c < M - 1 else -1 # 마지막이 아니면
            ]
            for nxt in adj:
                if nxt != -1 and tmp_world[nxt] == 0:
                    tmp_world[nxt] = 2
                    que.append(nxt)

        cur = not_wall - infection
        if ans < cur:
            ans = cur

    return ans


if __name__ == '__main__':
    print(solve())

'''
세로 크기 N 가로 크기 M (3 ≤ N, M ≤ 8)
0은 빈 칸, 1은 벽, 2는 바이러스
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
벽 3개 설치
벽 설치 백트래킹 쓰기
상 or 하 or 좌 or 우 == 0
    각각 2로 변경 
else:
    0의 개수 zido에 추가
    break

예제 입력 1 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1 
27
'''