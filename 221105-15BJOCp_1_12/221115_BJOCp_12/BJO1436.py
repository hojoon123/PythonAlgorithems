import sys
input =sys.stdin.readline

n = int(input())
num = 665
key = '666'
cnt = 0
while 1:
  num += 1
  if key in str(num):
    cnt += 1
    if cnt == n:
      break
print(num)
  

'''
처음 666
2 1666

 6이 적어도 3개이상 연속
0 < n <= 10000
N번째 영화의 제목에 들어간 수를 출력
예제 입력 1 
2
187
예제 출력 1 
1666
66666
'''