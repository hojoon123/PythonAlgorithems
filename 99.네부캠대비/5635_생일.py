import sys
input = sys.stdin.readline
    
def main():
    n = int(input())
    player = [list(map(str,input().rstrip().split())) for i in range(n)]
    player.sort(key= lambda x:(int(x[3]), int(x[2]), int(x[1])))
    print(player[-1][0])
    print(player[0][0])
    
if __name__ == "__main__":
    main()
    