from sys import stdin
input = stdin.readline

def check(n):
    print('F' if 9 in n else 'S')
    return
    
if __name__ == '__main__':
    n = map(int,input().split())
    check(n)
        
    

'''
예제 입력 1 
0 0 1 1 0 1 0 1
예제 출력 1 
S
'''