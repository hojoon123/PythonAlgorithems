import sys
input =sys.stdin.readline

t = int(input())
data = []
for i in range(t):
  h , w =map(int,input().split())
  data.append((h,w))
  
for i in range(t):
  cnt = 0
  for j in range(t):
    if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
      cnt += 1
  else:
    cnt += 1
    
  print(cnt, end= ' ')
      


'''
t h w
예제 입력 1 
5
55 185
58 183
88 186
60 175
46 155
예제 출력 1 
2 2 1 2 5
'''