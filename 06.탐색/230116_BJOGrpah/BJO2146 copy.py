from collections import deque
import sys
input = sys.stdin.readline

N = 0
answer = 1e9
drow, dcol = [-1,0,1,0],[0,1,0,-1]
visited = 0
def isLandBfs(board,row,col,idx):
	q = deque()
	q.append([row,col])
	while q:
		r,c = q.popleft()
		visited[r][c] = 1
		board[r][c] = idx
		for dr,dc in zip(drow,dcol):
			if 0 <= r+dr < N and 0 <= c+dc < N:
				if visited[r+dr][c+dc] == 0 and board[r+dr][c+dc] == 1:
					visited[r+dr][c+dc] = 1
					q.append([r+dr,c+dc])
				if board[r+dr][c+dc] == 0:
					board[r+dr][c+dc] = -1
					visited[r+dr][c+dc] = 1

def bridgeBfs(board,row,col,idx):
	q = deque()
	global visited
	visited = [[0]*N for _ in range(N)]
	q.append([row,col])
	length = 1
	while q:
		nextQ = deque()
		while q:
			r,c = q.popleft()
			if answer <= length:
				return 1e9
			visited[r][c] = 1
			for dr,dc in zip(drow,dcol):
				if 0 <= r+dr < N and 0 <= c+dc < N:
					if visited[r+dr][c+dc] == 0 and board[r+dr][c+dc] <= 0:
						nextQ.append([r+dr,c+dc])
						visited[r+dr][c+dc] = 1
					elif visited[r+dr][c+dc] == 0 and board[r+dr][c+dc] != idx and board[r+dr][c+dc] > 0:
						return length
		q = nextQ
		length += 1
	return 1e9

def solution():
	global N
	N = int(input())
	board = [list(map(int,input().split())) for _ in range(N)]
	global visited
	visited = [[0]*N for _ in range(N)]
	idx = 1
	for row in range(N):
		for col in range(N):
			if board[row][col] != 0 and visited[row][col] == 0:
				isLandBfs(board,row,col,idx)
				idx += 1
			visited[row][col] = 1

	global answer
	for row in range(N):
		for col in range(N):
			if board[row][col] == -1:
				for dr,dc in zip(drow,dcol):
					if 0 <= row+dr < N and 0 <= col+dc < N:
						if board[row+dr][col+dc] > 0:
							answer = min(bridgeBfs(board,row,col,board[row+dr][col+dc]),answer)
							break
	print(answer)

if __name__ == "__main__":
	solution()

'''
섬 찾기 섬 주위에 0들을 2로 바꾸고 카운트 증가 시키기
0이면 3으로 증가 시키기 반복 만약 1이 
예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
'''