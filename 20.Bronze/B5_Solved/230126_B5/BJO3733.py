from sys import stdin
#input = stdin.readline

def check():
    while 1:
        try:
            n, s = map(int,input().split())
            print(s // (n + 1))
        except:
            exit()
    
if __name__ == '__main__':
    check()
        
    

'''
예제 입력 1 
1 100
2 7
10 9
10 10
예제 출력 1 
50
2
0
0
'''