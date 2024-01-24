from sys import stdin
input = stdin.readline

def check(a, c):
    #a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
    b = [c[0] - a[2], c[1] // a[1], c[2] - a[0]]
    print(*b)
    
if __name__ == '__main__':
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    check(a, c)
        
    
    
'''
a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
a 🍰 b = c
2 2 75
예제 입력 1 
15 16 17 a
19 32 90 c
예제 출력 1 
2 2 75
'''