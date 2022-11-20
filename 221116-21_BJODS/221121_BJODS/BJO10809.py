import sys
input = sys.stdin.readline

s = list(input().rstrip())
alpha = [0] * 26
for i in s:
    alpha[ord(i)-97] += 1
print(*alpha)

''''97 122
첫째 줄에 단어 S
단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력
예제 입력 1 
baekjoon
예제 출력 1 
1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
'''