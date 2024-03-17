N = int(input())
numbers = list(map(int, input().split()))

stack = [];answer =[-1] * N

# solution
for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
'''
손코딩 돌려서 이해함. 내가 풀이한 코드는 17928을 들어가면 볼 수 있는데, 해당 코드는
for문 안에서 한 수 마다 j+1의 수와 비교해서 수 마다 큰 수를 찾을 때까지 연산함
최선의 경우 o(n)의 시간 복잡도를 가지지만, 최악의 경우 n**2임 무조건 시간초과가 나올 수 밖에
없는 구조. 그런데 해당 코드는 일단 바로 앞의 수랑만 비교하고 만약 아니다 싶으면 일단
다음 수를 연산함 stack안에 남은 수를 킵해두고
이렇게 되면 일단 가능한 거만 쭉 연산하고 그러다가 큰 수 하나 나오면 거기서 봇물 터져서
쿠콰콰쾅하고 한 번에 연산 때림 이러면 시간복잡도 O(n)따리일텐데 되게 가성비 코드
어마어마함

예제 입력 1 
4
3 5 2 7
예제 출력 1 
5 7 7 -1
'''