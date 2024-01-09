import sys
input = sys.stdin.readline

def minimize(value_arr, k):
    total_coin = 0
    for i in value_arr[::-1]:
        cur_coin = k // i
        k = k % i
        total_coin += cur_coin
    return total_coin
        

if __name__ == '__main__':
    n, k = map(int,input().split())
    coin_value = [int(input()) for i in range(n)]
    print(minimize(coin_value, k))


'''
N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000
N개의 줄에 동전의 가치 Ai가 오름차순
예제 입력 1 
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 1 
6
'''