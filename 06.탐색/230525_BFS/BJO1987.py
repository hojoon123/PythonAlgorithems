import sys
input = sys.stdin.readline

def bfs():
    global cnt
    # 요래 하면 0, 0, C를 하나로 봄ㅇㅇ 그래서 set에 0이 안 씹히게 해줌ㅇㅇ
    q = set([(0, 0, board[0][0])]) 
    
    while q:
        x, y, key = q.pop()
        
        cnt = max(cnt, len(key))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in key:
                # 넣을 때는 튜플로 넣을 거라 ㄱㅊ
                q.add((nx, ny, board[nx][ny] + key)) # 전에 꺼에 다음 꺼 붙여서 함
                # C -> AC 이렇게 붙여서 비교 그래서 not inㅇㅇ


if __name__ == '__main__':
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    n, m = map(int,input().split())
    board = [list(map(str,input().rstrip())) for i in range(n)]
    bfs()
    print(cnt)

'''
세로 R칸, 가로 C칸
대문자 알파벳
좌측 상단 칸 (1행 1열) 에는 말
말은 상하좌우로 인접한 네 칸 중의 한 칸
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야
같은 알파벳이 적힌 칸을 두 번 지날 수 없다
말이 최대한 몇 칸을 지날 수 있는지

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3
예제 입력 2 
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2 
6
'''