from math import gcd
n, s = map(int,input().split())
bro = list(map(int,input().split()))
a = [0] * n; j = 0
for i in range(n): a[i] = abs(s - bro[i])
tmp = a[0]
for i in range(1,n):
    tmp = gcd(tmp,a[i])
print(tmp)
'''
보자마자 최대공약수 떠올려야 했는데 시간초과 나고나서 생각이 나는 빠악빠악까악까악끄엑끄엑
알고리즘 넘 재밌어용 근데 넘 하기 싫어용 으ㅏㅇ르아르아르알ㅇㄹ아릉라ㅏ
절대값 해서 각자 거리 구하고 제일 작은 수부터 1씩 빼가면서 체크
첫째 줄에 N(1 ≤ N ≤ 105)과 S(1 ≤ S ≤ 109)
둘째 줄에 동생의 위치 Ai(1 ≤ Ai ≤ 109)
예제 입력 1 
3 3
1 7 11
예제 출력 1 
2
예제 입력 2 
3 81
33 105 57
예제 출력 2 
24
예제 입력 3 
1 1
1000000000
예제 출력 3 
999999999
'''