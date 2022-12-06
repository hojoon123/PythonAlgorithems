import sys

input = sys.stdin.readline

n = int(input())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(input())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)   

    
''''
입력 값이 10000까지로 제한 되면 이런 식으로 하는게 훨씬 효율적이겠다
예제 입력 1 
5
5
2
3
4
1
예제 출력 1 
1
2
3
4
5
'''