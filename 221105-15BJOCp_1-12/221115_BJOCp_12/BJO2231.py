import sys
input =sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n + 1):
  tmp = i + sum(map(int,str(i)))

  if tmp == n:
    result = i
    break

print(result)

'''
생성자 판별 프로그램
10의자리부터
10 1 0 11의 생성자 10 
n+ n의 자리수
 N(1 ≤ N ≤ 1,000,000)
생성자가 없는 경우에는 0을
예제 입력 1 
216
예제 출력 1 
198
'''