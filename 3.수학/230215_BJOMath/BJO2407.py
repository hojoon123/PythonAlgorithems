import sys
import math
input = sys.stdin.readline

def combi(n,m):
    parents = math.factorial(n)
    child = (math.factorial(n - m)) * (math.factorial(m))
    return parents // child



if __name__ == '__main__':
    n, m = map(int,input().split())
    print(combi(n,m))
    
    
'''
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)
nCm을 출력한다.
예제 입력 1 
100 6
예제 출력 1 
1192052400
'''