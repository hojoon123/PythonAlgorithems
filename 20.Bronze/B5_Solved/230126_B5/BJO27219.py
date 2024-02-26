from sys import stdin
input = stdin.readline

def check(n):
    print('V' * (n // 5), 'I' * (n % 5), sep = '')
        
    
if __name__ == '__main__':
    n = int(input())
    check(n)
        
    

'''
예제 입력 1 
13
예제 출력 1 
VVIII
'''