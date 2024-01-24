import sys
import math
input = sys.stdin.readline

def check(l,a,b,c,d):
    n1 = math.ceil(a / c)
    n2 = math.ceil(b / d)
    return (l - max(n1,n2))
            
if __name__ == '__main__':
    l = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(check(l,a,b,c,d))
    

'''
방학 총 일수 / 국어 A / 수학 B / 상하국최대 C / 수최 D
 L, A, B, C, D가 주
 항상 방학 숙제를 방학 기간내에 다 할 수 있는 경우만 입력
 첫째 줄에 상근이가 놀 수 있는 날의 최댓값을 출력
예제 입력 1 
20
25
30
6
8
예제 출력 1 
15
'''