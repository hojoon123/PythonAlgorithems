import sys
input = sys.stdin.readline

def check():
    while True:
        n = float(input())
        if n == 0: break
        print('{:.2f}'.format(1 + n + n**2 + n**3 + n**4))
    
if __name__ == '__main__':
    check()
    

'''
예제 입력 1 
3
40 62 77
88 62 77
91 33 18
예제 출력 1 
Gnomes:
Ordered
Unordered
Ordered
'''