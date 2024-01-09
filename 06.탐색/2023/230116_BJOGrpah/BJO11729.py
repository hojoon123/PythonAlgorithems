from sys import stdin
input = stdin.readline

def func(x, start, end):
    if x == 1 :
        print(start, end)
        return
    func(x - 1, start, 6 - start - end)
    print(start, end)
    func(x - 1, 6 - start - end, end)

n = int(input())
print(2 ** n - 1)
func(n, 1, 3)
'''
인덱스 0 에서 2로 옮기기
 N (1 ≤ N ≤ 20)이
 옮긴 횟수 K를 출력
A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로
예제 입력 1 
3
예제 출력 1 
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''