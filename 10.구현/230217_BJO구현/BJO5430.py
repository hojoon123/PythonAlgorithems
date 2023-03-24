import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(str,input().rstrip()))
        n = int(input())
        cnt = 0
        arr = deque(map(str,input().rstrip(']\n').lstrip('[').split(',')))
        if n == 0:
            arr = []
            # 여기서 바로 continue 걸었던게 패착
            # 문제를 잘 읽자 진짜 비었어도 D가 없으면 에러 안뜸 내 머리에 에러 떠서 죽을 뻔
        
        for func in s:
            if func == 'R':
                cnt += 1
            elif func == 'D':
                if len(arr) == 0:
                    print('error')
                    break
                else:
                    if cnt % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()
                    
        else:
            if cnt % 2 == 0:
                print('[' + ','.join(arr) + ']')
            else:
                arr.reverse()
                print('[' + ','.join(arr) + ']')
        
        
'''
함수 R(뒤집기)과 D(버리기)
R은 배열에 있는 수의 순서를 뒤집는 함수
D는 첫 번째 수를 버리는 함수
배열이 비어있는데 D를 사용한 경우에는 에러가 발생

 배열에 들어있는 수의 개수 n
 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수
예제 입력 1 
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
예제 출력 1 
[2,1]
error
[1,2,3,5,8]
error
'''