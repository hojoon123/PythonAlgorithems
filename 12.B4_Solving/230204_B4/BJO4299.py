from sys import stdin
input = stdin.readline

def check(a,b):
    x = (a - b) // 2
    y = a - x
    print(y, x)
    # x + y  = a  |x - y| = b
    # x = a - y   a - b = |-2y| 
    # y = 1 x = 2
if __name__ == '__main__':
    a, b = map(int,input().split())
    if a - b < 0 or (a - b):
        print(-1)
    else:
        check(a,b)
        
    

'''
예제 입력 1 
3 1
예제 출력 1 
2 1
'''