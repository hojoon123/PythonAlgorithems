from sys import stdin
input = stdin.readline

def check(s):
    if 6 <= len(s) <= 9: 
        return 'yes'
    else:
        return 'no'
    
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = str(input().rstrip())
        print(check(s))
        
    

'''
예제 입력 1 
3
1245125
asdij
120318739721
예제 출력 1 
yes
no
no
'''