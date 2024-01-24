from sys import stdin
input = stdin.readline

def check(n, a, k):
    a, k = int(a), int(k)
    if a > 17 or k >= 80:
        print(n,'Senior')
    else:
        print(n, 'Junior')
    
if __name__ == '__main__':
    while 1:
        n, a, k = map(str,input().split())
        if n == '#':
            break
        check(n, a, k)
        
    

'''
예제 입력 1 
Joe 16 34
Bill 18 65
Billy 17 65
Sam 17 85
# 0 0
예제 출력 1 
Joe Junior
Bill Senior
Billy Junior
Sam Senior
'''