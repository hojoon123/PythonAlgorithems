import sys
input = sys.stdin.readline
#너무 친절한 문제 11005 + 2745 합치면 끝
tmp = [] ; sum = 0; ans = []
for i in range(31): tmp.append(i)

A, B = map(int,input().split())
n = int(input()) 
numbers = list(map(int,input().split()))
numbers.reverse()

for i in range(n):
    sum += tmp.index(numbers[i]) * (A**i)
    
while sum != 0:
    ans.append(str(tmp[sum % B]))
    sum = sum // B
print(*ans[::-1])

'''
A진법을 입력받고 B진법으로 바꿔라
A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 2**20 보다 작음
A 로 줄테니 B로 바꿔라
A B 2이상 30이하
A진법으로 나타낸 숫자의 자리수의 개수 m(1 ≤ m ≤ 25)
A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터
예제 입력 1 
17 8
2
2 16
예제 출력 1 
6 2
'''