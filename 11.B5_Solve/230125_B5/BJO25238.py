from sys import stdin
input = stdin.readline

def check(a, b):
    if a - (a * (b / 100)) >= 100:
        print(0)
    else:
        print(1)
    
if __name__ == '__main__':
    a, b = map(int,input().split())
    check(a, b)
        
    

'''
예제 입력 1 
200 20
예제 출력 1 
0

'''