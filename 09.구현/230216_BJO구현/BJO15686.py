import sys
from itertools import combinations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bf():
    n,  m = map(int,input().split())
    city = [list(map(int,input().split())) for i in range(n)]
    answer = 10 ** 9
    house_arr = []
    chicken_arr = []

    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house_arr.append([i,j])
            elif city[i][j] == 2:
                chicken_arr.append([i,j])
                
    for chicken in combinations(chicken_arr, m):
        total_dist = 0
        for house in house_arr:
            dist = 1000
            for k in range(m):
                cur_dist = abs(house[0] - chicken[k][0]) + abs(house[1] - chicken[k][1])
                if cur_dist < dist:
                    dist = cur_dist
                    
            total_dist += dist
        if total_dist < answer:
            answer = total_dist
    return answer


if __name__ == '__main__':
    print(bf())
                


'''
백트래킹으로 치킨집 지우고 하나씩 넣어서 해보기
연구소랑 동일한 방식이죠
0은 빈 칸, 1은 집, 2는 치킨집
m개 남겨두고 폐업
치킨 집의 개수를 세고
예제 입력 1 
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
예제 출력 1 
5
예제 입력 2 
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
예제 출력 2 
10
예제 입력 3 
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
예제 출력 3 
11
예제 입력 4 
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
예제 출력 4 
32
'''