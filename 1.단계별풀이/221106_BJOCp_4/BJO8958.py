a = int(input())
b = []
for i in range(a):
    b.append(str(input()))
    totalScore = 0
    score = 0
    for j in b[i]:
        if(j == 'O'):
            score+= 1
            totalScore+= score
        else:
            score = 0
    print(totalScore)

'''
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
첫째 줄에 테스트 케이스의 개수
각 테스트 케이스는 문자열
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
테스트 케이스마다 점수를 출력
10
9
7
'''