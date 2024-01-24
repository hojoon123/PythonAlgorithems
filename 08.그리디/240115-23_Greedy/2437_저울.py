import sys
input = sys.stdin.readline

def solve(chus, ans):
    for chu in chus:
        if ans < chu:
            break
        ans += chu
    return ans

def main():
    n = int(input())
    chus = sorted(map(int,input().split()))

    print(solve(chus, 1))
    
if __name__ == "__main__":
    main()
