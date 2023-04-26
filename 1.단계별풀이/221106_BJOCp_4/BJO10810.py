import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int,input().split())
    basket = [0] * n
    for i in range(m):
        fir, sec, ball = map(int,input().split())
        for j in range(fir -1, sec):
            basket[j] = ball
    print(*basket)
'''
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)
방법은 세 정수 i j k로 이루어져 있으며, 
i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻

1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 
공이 들어있지 않은 바구니는 0을 출력
예제 입력 1 
5 4
1 2 3
3 4 4
1 4 1
2 2 2
예제 출력 1 
1 2 1 1 0
'''