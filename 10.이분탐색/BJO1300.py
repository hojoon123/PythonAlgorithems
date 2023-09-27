from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())

start, end = 1, N ** 2
result = 0

if N ** 2 == K:
    print(K)

else:
    while(start < end):
        mid = (start + end)//2

        tmp = 0
        for i in range(1, N + 1):
            tmp += min(mid // i, N)
        
        if tmp >= K:
            end = mid
            result = mid
        elif tmp < K:
            start = mid + 1
    print(result)

'''
풀이
이분 탐색을 어떻게 접목시킬 지 고민이 많이 된 문제이다.
당연히 배열을 직접 만들어 정렬하여 찾는다면, 10^10 + logN 번 연산해야 할 것이므로 불가능하다.
따라서 배열이 없을 때에도 A[k]를 이분 탐색으로 찾아야 한다는 소리다.
문제를 조금 바꿔서 생각해야 한다.
배열 A의 k번째 수를 찾는 것이 아닌, 숫자 몇이 k번째 수가 될 것인지 찾는 문제이다.
k번째 수가 존재한다는 것은, k보다 작거나 같은 수가 k개 만큼 존재한다는 의미이다.
이를 이용해서 문제를 풀어보자.
n = 5일 경우 A는 위와 같이 구성된다.
여기서 예를 들어 k=10, 즉 A[10] 을 찾는다고 해보자.
이분 탐색을 할 것이므로 start, end, mid를 지정해야 한다.
start = 1end = n^2 = 25mid = (start + end)//2 = 13  이다.
이제 13보다 작거나 같은 숫자들을 찾는다.
i를 각 행의 시작 숫자라고 할 때,
min(13 // i, n) 의 합이 13보다 작거나 같은 숫자들이다.
위 공식으로 계산해보면 13보다 작거나 같은 숫자는 19개가 있다.
k = 10을 찾아야 하는데 19개이므로 오버카운트되었다.
따라서 end를 13으로 바꾸고 mid값을 7로 조정하고 다시 위의 과정을 반복하게 된다.
이런식으로 계산하다보면 mid가 5가 된다.
위 그림에서 5보다 작거나 같은 수는 총 10개이다.
따라서 mid = k = 10 이므로 A[10] = 5 이다.
'''