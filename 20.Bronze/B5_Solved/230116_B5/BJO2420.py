from sys import stdin
input = stdin.readline

def distance(a, b):
    print(abs(a - b))

if __name__ == '__main__':
    a, b = map(int,input().split())
    distance(a, b)


'''
예제 입력 1 
-2 5
예제 출력 1 
7
'''