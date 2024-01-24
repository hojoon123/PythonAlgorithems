import sys 
import heapq
input = sys.stdin.readline

def maximum_weight(heap_jewelrys, bags):
    result = 0
    #2개의 리스트가 모두 채워져 있을 때까지만 계속 반복
    while (heap_jewelrys and bags):
        jewelry = heapq.heappop(heap_jewelrys)
        for b in range(len(bags)):
            if jewelry[1] <= bags[b]:
                bags.pop(b)
                #가격이 높은 순서대로 넣기 위해 heapq에 넣을 떄 -를 붙여서 넣었으므로 더할 때 다시 -를 붙여줘야함
                result += (-jewelry[0])
                break
            else:
                continue
                
    return result

def main() :
    #보석의 개수, 가방의 개수
    num_jewelry, num_bag = map(int, input().split())
    
    #보석의 무게, 가격 -> 보석의 개수만큼
    #heapq로 최댓값부터 꺼내주기 위해 (-가격, 무게)형태로 저장
    heap_jlist = []
    for _ in range(num_jewelry):
        weight, price = map(int, input().split())
        heapq.heappush(heap_jlist, (-price, weight))
        
    #가방에 담을 수 있는 최대 무게 -> 가방의 개수만큼
    heap_blist = sorted(int(input())for i in range(num_bag))
    
    print(maximum_weight(heap_jlist, heap_blist))

if __name__ == "__main__" : 
    main()