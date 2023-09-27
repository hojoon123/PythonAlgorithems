import sys
from math import sqrt
input = sys.stdin.readline
target = int(input())
N = list(map(int,str(target)))

M = int(input())
ben_nums = list(map(int,input().split()))
rest_nums = [0,1,2,3,4,5,6,7,8,9]
[rest_nums.remove(ben_nums[i]) for i in range(M)]
cnt = 0
ch = 0
tmp, tmp2 = 0, 0
num_list = []
if M == 0: 
    print(len(N))
    exit()
elif M < 9:
    cnt += len(N)
    for i in range(len(N)):
        if N[i] in ben_nums:
            for j in range(len(rest_nums)):
                num_list.append(abs(rest_nums[j] - N[i])) 
            min_idx = num_list.index(min(num_list)) # tmp에 가장 가까운 수 2개를 담음
            tmp = rest_nums[min_idx]
            rest_nums.pop(min_idx)
            num_list.pop(min_idx)
            tmp2 = rest_nums[min_idx]
            
            if tmp > N[i]:
                tmp = tmp * (10 ** (len(N)-i-1))
            else: #tmp가 N[i] 보다 작으면
                tmp = (tmp+1) * (10 ** (len(N)-i-1)) - 1
            if tmp2 > N[i]:
                tmp2 = tmp2 * (10 ** (len(N)-i-1))
            else:
                tmp2 = (tmp2+1) * (10 ** (len(N)-i-1)) - 1

            for k in range(len(N)-1, i-1, -1):
                ch += N[k] * (10 ** (len(N)-k-1))
                
            if abs(ch - tmp) > abs(ch - tmp2):
                cnt += ch - tmp2
            else:
                cnt += ch - tmp
            print(cnt)
            exit()

            

'''
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