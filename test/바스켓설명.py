import sys
input = sys.stdin.readline

n,m = map(int,input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m):
    i,j,k = map(int,input().split())
    basket = basket[:i-1] + basket[k-1:j] + basket[i-1:k-1] + basket[j:]
print(*basket)

'''
예제 입력 1 
10 5
1 6 4
3 9 8
2 10 5
1 3 3
2 6 2
예제 출력 1 
1 4 6 2 3 7 10 5 8 9
'''