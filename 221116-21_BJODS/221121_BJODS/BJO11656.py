import sys
input = sys.stdin.readline

s = list(input().rstrip())
stack = []

for i in range(len(s)):
    stack.append(''.join(s))
    s.pop(0)
stack.sort()
print(*stack,sep= '\n')
'''
예제 입력 1 
baekjoon
예제 출력 1 
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
'''