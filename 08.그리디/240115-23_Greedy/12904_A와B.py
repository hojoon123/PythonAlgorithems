import sys
input = sys.stdin.readline

def solve(s, t):
    check = False
    while t:
        if t[-1] == "A":
            t.pop()
        else:
            t.pop()
            t.reverse()
        if s == t:
            return 1
    
    return 0

def main():
    s = list(map(str,input().rstrip()))
    t = list(map(str,input().rstrip()))

    print(solve(s, t))
    
if __name__ == "__main__":
    main()
