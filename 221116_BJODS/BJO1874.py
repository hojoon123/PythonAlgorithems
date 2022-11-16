import sys
input = sys.stdin.readline

n = int(input())
stack = []
op = []
cnt = 1
temp = True
for i in range(n):
    num = int(input()) 
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

'''
첫 줄에 n (1 ≤ n ≤ 100,000)
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력
push연산은 +로, pop 연산은 -로 표현
불가능한 경우 NO를 출력
'''