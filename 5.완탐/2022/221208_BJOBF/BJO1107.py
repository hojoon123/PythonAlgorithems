import sys
from math import sqrt
input = sys.stdin.readline
target = int(input())
M = int(input())
ben_nums = list(map(int,input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in ben_nums:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))            
print(min_count)
'''
다시 해보기
고민 겁나 싸고 개망함
N (0 ≤ N ≤ 500,000)
M (0 ≤ M ≤ 10)
셋째 줄에는 고장난 버튼
예제 입력 1 
5457
3
6 7 8
예제 출력 1 
6
'''