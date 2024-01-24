import sys
input = sys.stdin.readline

def check(n):
    r = n % 8
    c = n // 8
    tmp = ''
    if r == 0:
        tmp += row[-1]
        tmp += col[c - 1]
    else:
        tmp += row[r - 1]
        tmp += col[c]
    
    
    return tmp
if __name__ == '__main__':
    n = int(input())
    row = 'abcdefgh'
    col = '12345678'
    print(check(n))
        
    

'''
예제 입력 1 
1
예제 출력 1 
a1
'''