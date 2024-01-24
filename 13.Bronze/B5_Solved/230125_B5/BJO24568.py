from sys import stdin
input = stdin.readline

def check(a, b):
    print((a * 8 + b * 3) - 28)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    check(a, b)
        
    

'''
is 2 × 8 + 5 × 3 whi
예제 입력 1 
2
5
예제 출력 1 
3

'''