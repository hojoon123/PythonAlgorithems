n, m = map(int,input().split())
#5의 개수 세야됨
#n! / (n-m)! * m!
def cal5(num):
    a = 5; cnt = 0
    while num >= a:
        cnt += num//a
        a *= 5
    return cnt
def cal2(num):
    a = 2; cnt = 0
    while num >= a:
        cnt += num//a
        a *= 2
    return cnt
tmp = cal5(n) - (cal5(n-m) + cal5(m))
tmp2 = cal2(n) - (cal2(n-m) + cal2(m))
if tmp > tmp2:
    print(tmp2)
else:
    print(tmp)
'''
0의 개수 10의 배수 2 x 5 라고 할 수도 있음
2와 5의 계수 중 더 낮은 거를 출력하면 됨
왜냐 2 x 5 가 10이라서 0의 개수 때리려면
2**3 x 5** 4 = 3이다 이거임ㅇㅇ
n! / (n-m)! * m!
첫째 줄에 정수 n, m (0 <= m <= n <= 2,000,000,000, n != 0)
예제 입력 1 
25 12
예제 출력 1 
2
'''