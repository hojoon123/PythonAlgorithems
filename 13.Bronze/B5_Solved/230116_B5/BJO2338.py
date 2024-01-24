from sys import stdin
input = stdin.readline

def sum(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum(a, b)


'''
예제 입력 1 
1
-1
예제 출력 1 
0
2
-1
'''