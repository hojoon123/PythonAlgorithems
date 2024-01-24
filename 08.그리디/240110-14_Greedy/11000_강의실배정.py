import sys
import heapq
input = sys.stdin.readline

def solve(time, room, n):
    heapq.heappush(room, time[0][1])
    
    for i in range(1, n):
        if time[i][0] < room[0]:
            heapq.heappush(room, time[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, time[i][1])
    return len(room)
    

def main():
    n = int(input())
    time = [list(map(int,input().split())) for i in range(n)]
    time.sort()
    room = []

    print(solve(time, room, n))
    
if __name__ == "__main__":
    main()
