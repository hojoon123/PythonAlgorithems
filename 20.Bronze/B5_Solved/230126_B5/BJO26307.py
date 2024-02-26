from sys import stdin
input = stdin.readline

def check(h, m):
    return (h - 9) * 60 + m
    
if __name__ == '__main__':
    h, m = map(int,input().split())
    print(check(h, m))
        
    

'''
예제 입력 2 
11 59
예제 출력 2 
179
'''