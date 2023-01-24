from sys import stdin
input = stdin.readline

def check(n, f):
    a = int(n[:-2] + '00')
    while True:
        if a % f == 0:
            break
        a += 1
    print(str(a)[-2:])

if __name__ == '__main__':
    n = str(input().rstrip())
    f = int(input())
    check(n, f)

'''
예제 입력 1 
1000
3
예제 출력 1 
02
'''