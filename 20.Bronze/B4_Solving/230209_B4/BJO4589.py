from sys import stdin
input = stdin.readline

def check(abc):
    if sorted(abc) == abc or sorted(abc, reverse = True) == abc:
        print('Ordered')
    else:
        print('Unordered')
    
if __name__ == '__main__':
    n = int(input())
    print('Gnomes:')
    for i in range(n):
        abc = list(map(int,input().split()))
        check(abc)
        
    

'''
예제 입력 1 
3
40 62 77
88 62 77
91 33 18
예제 출력 1 
Gnomes:
Ordered
Unordered
Ordered
'''