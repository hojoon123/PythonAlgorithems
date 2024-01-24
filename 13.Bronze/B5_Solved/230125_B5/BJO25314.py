from sys import stdin
input = stdin.readline

def check(n):
    text = 'long '
    print(text * (n//4),'int', sep = '')
    
if __name__ == '__main__':
    n = int(input())
    check(n)
        
    

'''
예제 입력 2 
20
예제 출력 2 
long long long long long int
'''