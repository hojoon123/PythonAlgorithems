from sys import stdin
input = stdin.readline

def change(s):
    print(s.swapcase())

if __name__ == '__main__':
    s = str(input().rstrip())
    change(s)


'''
예제 입력 1 
WrongAnswer
예제 출력 1 
wRONGaNSWER
'''