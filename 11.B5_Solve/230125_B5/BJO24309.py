from sys import stdin
input = stdin.readline

def check(a, b, c):
    print((b - c) // a)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    check(a, b, c)
        
    

'''
예제 입력 1 
4
20
8
예제 출력 1 
3

'''