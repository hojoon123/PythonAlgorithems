import sys
input =sys.stdin.readline

m , n = map(int,input().split())
board = []
result = []
for _ in range(m):
  board.append(input().rstrip())
  
for i in range(m-7): #8칸으로 자르니까 뭐가 오든 7을 뺌 시작지점이기 때문 아래 for문에서 8번 할거라
  for j in range(n-7):
    startB = 0
    startW = 0
    for a in range(i,i+8):
      for b in range(j,j+8):
        if (a + b) % 2 == 0: #홀수짝수로 나눔 짝수면 a[0][0] a[0][2], a[1][3] 등 칸을 보는 것
          if board[a][b] != 'W': # W든 B든 상관 없음 중요한 건 startW , B 등 시작할 때
            startW += 1         # 얘네가 W 축이냐 B 축이냐를 봐야함
          else:                 # B시작이라 가정하면 홀수칸은 무조건 W가 되어야 함.
            startB += 1         # 그래서 a+b % 2 의 else 문을 보면 W가 아니면 b시작의 카운트+1
        else:                   # 홀수 칸이 B일때 W로 칠해버리는 거임ㅇㅇ W면 냅두고
          if board[a][b] != 'W':# 이렇게 시작지점 기준으로 for 문 돌려서 가장 적게 바꿔도 되는 값을 찾음
            startB += 1
          else:
            startW += 1

    result.append(startB)
    result.append(startW)
 
print(min(result))

  


'''
if b[i] == b[i+1]
cnt+=1
else:
tmp = cnt
cnt = 0
N과 M
8 <= n,m <= 50
n개의 줄 n개의 원소
B는 검은색이며, W는 흰색
다시 칠해야 하는 정사각형 개수의 최솟값을 출력
예제 입력 1 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
예제 출력 1 
1
'''