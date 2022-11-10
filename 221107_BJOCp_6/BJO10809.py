a = input()
b = list(range(97,123))  # 아스키코드 숫자 범위

for i in b:
    print(a.find(chr(i)), end =" ") 
'''
hooooojoon
예제 입력 1 
baekjoon
예제 출력 1 
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
0부터 순차
'''