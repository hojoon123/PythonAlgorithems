import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1  
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')
#보고 깜짝놀란 코드 시간이 궁금해서 체크
#빠를 건 예상했지만 deque를 사용한 코드보다 무려 40배 빨랐음
#deque의 시간복잡도는 O(n)인 것 같고 해당 코드는 O(1)이라고 생각함

'''

3번째 사람 빼기 123 456 712 457 
예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
'''