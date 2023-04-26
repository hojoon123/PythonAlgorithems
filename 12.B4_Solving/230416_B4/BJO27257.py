import sys
input = sys.stdin.readline

def check():
    global n
    tmp = list(n)
    for i in tmp:
        if i == '0':
            n.pop(0)
        
        else:
            print(n.count('0'))
            return
    
if __name__ == '__main__':
    n = list(map(str,input().rstrip()))
    n.reverse()
    check()
        
    

'''
예제 입력 1 
100500
예제 출력 1 
2
'''