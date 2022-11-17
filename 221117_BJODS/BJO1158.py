import sys
from collections import deque

input = sys.stdin.readline

n , k = map(int,input().split())
arr = deque()
[arr.append(i) for i in range(1,n+1)]
result = []

while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())
print(str(result).replace('[','<').replace(']','>'))

#arr.append(str(arr.pop(num)))
#print("<",", ".join(arr),">", sep='') 시간 차이는 별로 안 나는데, 미세하게 replace가 더 빠름
#무엇보다 replace가 이 경우에는 조금 더 사용하기 편한 것 같음
'''

3번째 사람 빼기 123 456 712 457 
예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
'''