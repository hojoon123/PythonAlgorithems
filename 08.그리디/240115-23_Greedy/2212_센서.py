import sys
input = sys.stdin.readline

# 센서와 집중국 정렬된 센서 리스트를 넣으면 센서와 집중국 사이 거리의 최소값을 구해주는 함수
def solve(n, k, sensor):
    if k >= n:
        return 0
    dist = []
    for i in range(1,n):
        dist.append(sensor[i] - sensor[i-1])
    dist.sort()
    
    for i in range(k - 1):
        dist.pop()
    ans = sum(dist)
    return ans

def main():
    n = int(input())
    k = int(input())
    sensor = sorted(map(int,input().split()))

    print(solve(n,k,sensor))
    
if __name__ == "__main__":
    main()
