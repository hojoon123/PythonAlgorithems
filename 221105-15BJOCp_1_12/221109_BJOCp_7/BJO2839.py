import sys

input = sys.stdin.readline
n = int(input())

a = [5001] * (n+5)
a[3] = a[5] = 1

for i in range(6, n+1):
    a[i] = min(a[i-3], a[i-5]) + 1

print(a[n] if a[n] < 5001 else -1)
'''
a 배열은 N킬로그램일 때, 각각 가장 적은 양의 봉지를 담을 용도로 사용된다.
최소 값 구해야하기 때문에 N의 범위보다 하나 큰 값이 "5001"을 값으로 지정한다. 
index 3, 5에는 각각 1개의 봉지를 사용하고 최초의 값으로 이용하기 위해 "1"을 대입한다.
배열의 크기를 "n+5"로 잡은 이유는... N의 값이 5보다 작은 경우 Index Out of Range 
오류를 잡기 위해서다.
배열이 5와 같거나 보다 작은 경우는 이미 결과가 저장되어있기 때문에
for문의 range는 6부터 시작한다.
6부터는 해당 위치보다 "-3", "-5"의 위치 중 작은 값을 갖고와서 1을 더하면 
해당 위치에서 가장 적은 양의 봉지를 구할 수 있다. 
N킬로그램을 만들 수 없으면 a배열값이 5000보다 크기 때문에 치환해서 -1을 반환한다.


반례
마지막 출력부분에서 a[n] != 5001 이런식으로하면 반례가 발생한다.
N이 7인 경우... 7-3=4, 7-5=2 --> 2, 4 모두 5001이 기본값이기 때문에 5002가 답으로 반환될 수 있다.


18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한ㄷr.
예제 입력 1 
18
예제 출력 1 
4
'''