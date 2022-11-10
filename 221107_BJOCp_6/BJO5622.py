import string

a = list(map(str,input()))
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
currentTime = 0

for i in a:
    for j in b:
        if i in j:
            currentTime += b.index(j)+3

print(currentTime)
'''
2부터 2초+n당1초 2~6 3자리 7 4자리 8 3자리 9 4자리
2 0~2 3 3~5 4 6~8 5 9~11 6 12~14 7 15~18 8 19~21 9 22~25
예제 입력 1 
WA
예제 출력 1 
13
'''