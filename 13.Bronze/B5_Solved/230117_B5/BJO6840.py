from sys import stdin
input = stdin.readline

def check():
    n = [0] * 3
    for i in range(3):
        n[i] = int(input())
        
    n.sort()
    print(n[1])

if __name__ == '__main__':
    check()
    
    
'''
예제 입력 1 
10
5
8
예제 출력 1 
8
'''