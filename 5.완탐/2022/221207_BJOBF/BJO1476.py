import sys
from math import sqrt
input = sys.stdin.readline
year = 0
E, S, M = map(int,input().split())
ET, ST, MT = 0, 0, 0
while 1:
    year += 1
    ET += 1; ST += 1; MT += 1
    if E == ET and S == ST and M == MT:
        print(year)
        exit()
    if year % 15 == 0:
        ET = 0
    if year % 28 == 0:
        ST = 0
    if year % 19 == 0:
        MT = 0
'''
세 수 E, S, M
E S M으로 표시되는 가장 빠른 연도를 출력
예제 입력 1 2 3
1 16 16
1 1 1
1 2 3
예제 출력 1 2 3
1
16
5266
'''