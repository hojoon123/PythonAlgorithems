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