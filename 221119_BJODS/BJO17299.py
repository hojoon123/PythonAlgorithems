import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
dict = {}; stack = []; answer = [-1] * n
cnt = 0
for i in numbers: #딕셔너리로 numbers를 카운팅 함.
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    cnt += 1

for i in range(n): #17298번의 식을 그대로 사용하여 적용함 시간복잡도 O(n)
    while stack and dict[numbers[stack[-1]]] < dict[numbers[i]]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)
print(*answer)

'''
생각한대로 풀었음 확실히 앞의 문제와 유사한 문제라서 쉽게 품.
보자마자 딕셔너리로 카운트 해서 사용하자 느낌
문제 푸는 시간은 딕셔너리를 만들기 위해 초반에 한 번 돌린 만큼 전 문제에 비해 700초 늘어남
딕셔너리 보다 처음부터 그냥 다 만들어두고 하는게 더 빠르네
오등큰수
예제 입력 1 
7
1 1 2 3 4 2 1
예제 출력 1 
-1 -1 1 2 2 1 -1
'''