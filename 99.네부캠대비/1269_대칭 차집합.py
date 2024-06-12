import sys
input = sys.stdin.readline

def check(a,b):
    ans = 0 
    for i in a:
        if i in b:
            continue
        else:
            ans += 1
                
    for i in b:
        if i in a:
            continue
        else:
            ans += 1
    return ans

def main():
    n, m = map(int,input().split())
    a = dict()
    for i in list(map(int,input().split())):
        if i in a:
            continue
        else:
            a[i] = 1
    
    b = dict()
    for i in list(map(int,input().split())):
        if i in b:
            continue
        else:
            b[i] = 1
            
    print(check(a,b))
if __name__ == "__main__":
    main()