import sys

input = sys.stdin.readline

n , k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
print(arr[n-k])    

'''
첫째 줄에는 응시자의 수 n과 상을 받는 사람의 수 k
둘째 줄에는 각 학생의 점수 x
상을 받는 커트라인을 출력
예제 입력 1 
5 2
100 76 85 93 98
예제 출력 1 
98
'''