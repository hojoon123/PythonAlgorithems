from sys import stdin
input = stdin.readline

def check(a, b, c):
    return (((b // a) * 3) * c)
    
if __name__ == '__main__':
    a, b, c = map(int,input().split())
    print(check(a, b, c))
        
    

'''
예제 입력 1 
10 100 7
예제 출력 1 
210
'''