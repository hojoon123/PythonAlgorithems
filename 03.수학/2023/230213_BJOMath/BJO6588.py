import sys
input = sys.stdin.readline

arr = []
check = [0] * 1000001

for i in range(2, 1000001):
    if check[i] == 0:
        arr.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

while 1:
    b = int(input())
    if b == 0:
      exit()
    for i in range(1,len(arr)):
        if check[b - arr[i]] == 0:
            print(f'{b} = {arr[i]} + {b - arr[i]}')
            break
    
'''

'''