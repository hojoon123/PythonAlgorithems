import sys
input = sys.stdin.readline

arr = [1] * 11
arr[2] = 2; arr[3] = 4
for i in range(4,11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
for _ in range(int(input())):
    n = int(input())
    print(arr[n])
    
    #해당 경우는 n 11이하 나눈 경우


'''
i = i-1 i-2 i-3
t 
1 <=n <= 11
예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
'''