from sys import stdin
input = stdin.readline

def check(n):
    tmp = 0
    for i in range(n):
        tmp += int(input())
    return tmp
        
    
if __name__ == '__main__':
    n = int(input())
    print(check(n))
        
    

'''
예제 입력 1 
3
1
2
3
예제 출력 1 
6
'''