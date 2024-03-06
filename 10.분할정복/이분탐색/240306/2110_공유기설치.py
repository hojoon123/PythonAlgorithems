import sys
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline

def find_max_dist(n, c, graph):
    pass
            
def main():
    n, c = map(int,input().split())
    graph = [int(input()) for i in range(n)]
    print(find_max_dist(n, c, graph))
            
if __name__ =="__main__":
    main()
    


'''
예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''