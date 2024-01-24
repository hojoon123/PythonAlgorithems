import sys
input = sys.stdin.readline

def check(n, m):
    if n >= 8:
        print(n-7)
    else:
        print(m+7)
        
    return 
if __name__ == '__main__':
    n, m = map(int,input().split())
    check(n, m)
        
    

'''
n >= 15
print(n-7)
else
일요일 날짜 n 저저번주 m
31 26 
30 25 
29 24 
28 23
예제 입력 1 
9 24
2 
예제 출력 1 
2
'''