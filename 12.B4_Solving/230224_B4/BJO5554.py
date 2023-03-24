import sys
input = sys.stdin.readline

def check(a,b,c,d):
    total_sec = a + b + c + d
    result = []
    result.append(total_sec // 60)
    result.append(total_sec % 60)
    return result
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    ans = check(a,b,c,d)
    for i in ans:
        print(i)
        
    

'''
예제 입력 1 
31
34
7
151
예제 출력 1 
3
43
'''