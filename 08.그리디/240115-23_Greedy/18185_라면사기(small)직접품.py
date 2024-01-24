import sys
input = sys.stdin.readline

def solve(factory, n):
    ans = 0
    for i in range(n): # 오류 안 나는 범위까지만
        if factory[i] != 0:
            if factory[i+1] != 0:
                if factory[i+2] != 0:
                    # 2번째가 3번째 보다 크면 5부터 먼저 까주기
                    if factory[i+1] > factory[i+2]:
                        tmp = min(factory[i], factory[i+1] - factory[i+2])
                        for j in range(2):
                            factory[i+j] -= tmp
                        ans += tmp * 5
                        
                    # 3개씩 빼주고 7원씩 올리기
                    tmp = min(factory[i], factory[i+1], factory[i+2])
                    for j in range(3):
                        factory[i+j] -= tmp
                    ans += tmp * 7
                    
                # 나머지 2개씩 빼주고 5원씩 올리기
                if factory[i] != 0 and factory[i+1] != 0:
                    tmp = min(factory[i+j] for j in range(2))
                    for j in range(2):
                        factory[i+j] -= tmp
                    ans += tmp * 5
            # 나머지 다 빼고 3원 올리기
            if factory[i] != 0:
                tmp = factory[i]
                factory[i] = 0
                ans += tmp * 3
    return ans
    
def main():
    n = int(input())
    factory = list(map(int,input().split())) + [0,0]
    print(solve(factory, n))
    
if __name__ == "__main__":
    main()
