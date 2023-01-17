from sys import stdin
input = stdin.readline

def check():
    tmp = 0
    for i in range(5):
        n = int(input())
        tmp += n
    print(tmp)

if __name__ == '__main__':
    check()
    
    
'''
예제 입력 1 
1
2
3
4
5
예제 출력 1 
15
'''