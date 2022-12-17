import sys
from itertools import permutations
input = sys.stdin.readline
 
def func(num):
    for per in permutations(num,N+1):
        flag = True
        for i in range(len(s)):
            if s[i] == '<':
                if per[i] < per[i+1]: continue
                else:
                    flag = False
                    break
            
            else:
                if per[i] > per[i+1]: continue
                else:
                    flag = False
                    break
        
        if flag == True:
            print(''.join(map(str,per)))
            break

N = int(input())
s = list(map(str,input().split()))
num = [i for i in range(10)]
reverse_num = num[::-1]
res = []

func(reverse_num)
func(num)



'''

예제 입력 1 
2
< >
예제 출력 1 
897
021
'''