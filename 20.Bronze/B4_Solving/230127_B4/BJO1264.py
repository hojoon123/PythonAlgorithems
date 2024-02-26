from sys import stdin
input = stdin.readline

def check():
    arr = ['a', 'e', 'i', 'o', 'u']
    while 1:
        cnt = 0
        s = str(input().rstrip()).lower()
        if s == '#':
            break
        for i in arr:
            cnt += s.count(i)
        print(cnt)
    
if __name__ == '__main__':
    check()
        
    

'''
a', 'e', 'i', 'o', 'u'
예제 입력 1 
How are you today?
Quite well, thank you, how about yourself?
I live at number twenty four.
#
예제 출력 1 
7
14
9
'''