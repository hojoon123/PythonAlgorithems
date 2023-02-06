from sys import stdin
input = stdin.readline

def check(s, i):
    print('{0}.'.format(i), s)
    
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n + 1):
        s = str(input().rstrip())
        check(s, i)
        
    

'''
예제 입력 1 
5
Lionel Cosgrove
Alice
Columbus and Tallahassee
Shaun and Ed
Fido
예제 출력 1 
1. Lionel Cosgrove
2. Alice
3. Columbus and Tallahassee
4. Shaun and Ed
5. Fido
'''