import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a =list(map(str,input().split()))
    for j in a:
        print(j[::-1], end = ' ')


'''
 테스트 케이스의 개수 T
 단어의 길이는 최대 20, 문장의 길이는 최대 1000
 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다
예제 입력 1 
2
I am happy today
We want to win the first prize
예제 출력 1 
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
'''