def merge_sort(A, p, r):
    if(p < r and count <= K):
        q = (p + r) // 2
        merge_sort(A, p , q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        
def merge(A, p, q, r):
    global count, result
    i, j = p, q + 1
    tmp = []
    
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
        
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)


'''
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 108)
다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN
K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력
예제 입력 1 
5 7
4 5 1 3 2
예제 출력 1 
3
'''