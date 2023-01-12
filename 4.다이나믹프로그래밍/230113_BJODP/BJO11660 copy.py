from sys import stdin

input = stdin.readline
#이게 메모리 최소화 하고 if 문 존나 때려서 만든 거 
#numbers를 덧씌워서 메모리 최소화 게다가 number를 입력함과 동시에 numbers에 채워서 for문까지 덜 돌림
#나보다 훨씬 잘 짠 코드 진짜 배울게 많다...
def main():
    size, sum_count = map(int, input().split())
    numbers = []

    for i in range(size):
        row = []
        for j, number in enumerate(map(int, input().split())):
            delta = numbers[i-1][j] if i > 0 else 0
            mae = row[j-1] if j > 0 else 0
            diagonal = numbers[i-1][j-1] if i > 0 and j > 0 else 0

            row.append(delta + mae + number - diagonal)
        numbers.append(row)
        

    for _ in range(sum_count):
        y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())

        result = numbers[y2][x2]

        if x1 > 0:
            result -= numbers[y2][x1 - 1]
        if y1 > 0:
            result -= numbers[y1 - 1][x2]
        if x1 > 0 and y1 > 0:
            result += numbers[y1-1][x1-1]

        print(result)


if __name__ == '__main__':
    main()

'''
표의 크기 N과 합을 구해야 하는 횟수 M
N개의 줄에는 표에 채워져 있는 수
M개의 줄에는 네 개의 정수 x1, y1, x2, y2
M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력
예제 입력 1 
4 3

1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

2 2 3 4
3 4 3 4
1 1 4 4
예제 출력 1 
27
6
64
'''