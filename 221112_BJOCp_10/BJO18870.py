import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
b.sort()

dic = {b[i] : i for i in range(len(b))}
for i in a:
    print(dic[i], end = ' ')

#for i in a: 
    #print(b.index(i), end = ' ') O(n) 딕셔너리 한 번 다돌리고 바로바로 꺼내면 O(1)ㅇ이라
    #index로 매번 돌리면 O(n) 극단적으로 10억 찾고 11억 찾고 ㅈㄴ 사고가 발생함 너무 길어짐
'''
1 ≤ N ≤ 1,000,000
-10 9제곱 ≤ Xi ≤ 10 9제곱
예제 입력 1 
5
2 4 -10 4 -9
예제 출력 1 
2 3 0 3 1
'''