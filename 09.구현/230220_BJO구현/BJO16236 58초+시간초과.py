import sys
from collections import deque
input = sys.stdin.readline

def bfs(bs_loc, cnt, graph):
    global baby_shark, fish
    q = deque()
    q.append(bs_loc)
    exp = 0
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            
            if ocean[nr][nc] <= baby_shark: # 작거나 0일때
                if ocean[nr][nc] and baby_shark > ocean[nr][nc]: # 물고기 있을 때
                    exp += 1
                    print('남은 물고기:', fish)
                    print('먹을 좌표:', nr, nc)
                    fish.remove(ocean[nr][nc])
                    ocean[nr][nc] = 0
                    print('경험치:', exp)
                    print('현재 몸무게:', baby_shark)
                    if exp == baby_shark:# 베비샼몸무게추가
                        exp = 0
                        baby_shark += 1
                    cnt += abs(nr - bs_loc[0]) + abs(nc - bs_loc[1])
                    print('걸린 시간:', cnt)
                    print('먹은 좌표:', nr, nc)
                    print('먹은 몸무게:', baby_shark)
                    for i in range(n):
                        print(*ocean[i])
                    
                    if fish:
                        if baby_shark <= min(fish):
                            return cnt
                    else:
                        return cnt
                    
                    ocean[bs_loc[0]][bs_loc[1]] = 0
                    bs_loc[0] = nr; bs_loc[1] = nc
                    q.clear()
                    q.append(bs_loc)
                    break
                q.append([nr,nc])

if __name__ == '__main__':
    dr = [-1,0,1,0] # 0 상 1 좌 2 하 3 우
    dc = [0,-1,0,1]
    n = int(input())
    ocean = [list(map(int,input().split())) for i in range(n)]
    baby_shark = 2
    fish = []
    ready = 0
    for i in range(n):
        for j in range(n):
            if ocean[i][j] and ocean[i][j] != 9:
                fish.append(ocean[i][j])
            if ocean[i][j] == 9:
                baby_shark_location = [i,j]
                ocean[i][j] = 0
    if fish and baby_shark >= min(fish):
        print(bfs(baby_shark_location, 0, ocean))
    else:
        print(0)
    

'''
완벽함 만든 건 완벽한데
문제 이해를 잘못하고 만듬 씨이빨
진짜 혈압 개 오른다 ㅇㄹ이른ㅇ람히ㅡㅏㄱㄷ힉ㅈㅎㅈ기후ㅏ
나는 아무리 생각해도 13 초가 나오는데 왜 14초라는거지? 왜 60초지?
어떻게 해야 14초 60초가 나오는거야 ㄷ시ㅡㅂㅈ샇ㅂ갛지룾ㅁㅇㄴ라ㅜㅇㄴ럼나루
혈압 뒤지네 
는 같은 물고기는 못 먹는 걸 제대로 안 읽음 앙라느란을ㅇ나ㅡ랑ㄴ르ㅏ
근데 이후에 성공해서 14초는 떴는데 60초는 58초가 나오네ㅋㅋ;
더 이상 개선하기 힘들 정도... 그래도 해본다
원인발견
위쪽왼쪽 트리거에서 문제가 발생
상하좌우로 돌리기만 하는 것이 아니라
원래 위치 기준으로 여러 군데일시 순차적으로 도는 거임..
나는 다음 위치에서 새로 갱신하지만 현 위치에서 털고 가는 거였음...


위왼트리거거 첨에 4방을 위왼쪽부터 가도록 설계
아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다

아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다
크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다


먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
0: 빈 칸    
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
예제 입력 2 
3
0 0 1
0 0 0
0 9 0
예제 출력 2 
3
예제 입력 3 
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
예제 출력 3 
14
예제 입력 4 
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
예제 출력 4 
60
예제 입력 5 
6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
예제 출력 5 
48
예제 입력 6 
6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
예제 출력 6 
39
'''