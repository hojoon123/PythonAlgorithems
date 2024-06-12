import sys
input = sys.stdin.readline

def check(n, m):
    d = dict()
    for _ in range(n):
        site, password = map(str,input().rstrip().split())
        d[site] = password
    for _ in range(m):
        site = input().rstrip()
        print(d[site])
            

def main():
    n, m = map(int,input().split())
    check(n,m)
    
if __name__ == "__main__":
    main()