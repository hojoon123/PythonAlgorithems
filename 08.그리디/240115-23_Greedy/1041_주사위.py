import sys
input = sys.stdin.readline

def solve(n, dice):
    ans = 0
    min_nums = []
    
    if n == 1:
        dice.sort()
        ans = sum(dice[i] for i in range(5))
    else:
        min_nums.append(min(dice[0],dice[5]))
        min_nums.append(min(dice[1],dice[4]))
        min_nums.append(min(dice[2],dice[3]))
        min_nums.sort()
        
        side1 = min_nums[0]
        side2 = sum(min_nums[0:2])
        side3 = sum(min_nums)
        
        ans += (4 * (n-2) * (n-1) + (n-2)**2) * side1
        ans += (4 * (n-1) + 4 * (n-2)) * side2
        ans += 4 * side3
        
    
    return ans
def main():
    n = int(input())
    dice = list(map(int,input().split()))
    
    print(solve(n,dice))
    
if __name__ == "__main__":
    main()
