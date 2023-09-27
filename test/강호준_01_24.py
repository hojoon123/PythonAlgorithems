from sys import stdin
import heapq
input = stdin.readline

def priority_queue(q):
    sorted_list = []
    heapq.heapify(q)
    
    while q:
        sorted_list.append(heapq.heappop(q))
        
    return sorted_list

if __name__ == "__main__": # 메인문입니다.
    user_input = list(map(int,input().split())) # 공백 기준으로 한줄에 1 3 5 1 2 3 등 입력
    print(priority_queue(user_input))
    
'''
우선순위 큐 숫자 정렬

'''    