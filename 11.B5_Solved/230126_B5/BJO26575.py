from sys import stdin
input = stdin.readline

def check():
    n = int(input())
    for i in range(n):
        d, f, p = map(float, input().split())
        print('${:.2f}'.format(d * f * p))
        
    
if __name__ == '__main__':
    check()
        
    

'''
예제 입력 1 
3
3 2 1
5 .16 4.54
3 3.7 3.6
예제 출력 1 
$6.00
$3.63
$39.96
'''