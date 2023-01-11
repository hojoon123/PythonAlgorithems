import sys
input = sys.stdin.readline

def add(x):
    s.add(x)
    return
    
def remove(x):
    s.discard(x)
    return

        
def check(x):
    if x in s: print(1)
    else: print(0)
    
    return
    
def toggle(x):
        if x in s: s.remove(x)
        else: s.add(x)
        
        return
def all():
    for i in range(1,21): s.add(i)
    
    return
def empty():
    s.clear()
    return

s = set()
N = int(input())
for i in range(N):
    order = list(map(str,input().split()))
    
    if len(order) == 1:
        if order[0] == 'all':
            all()
        if order[0] == 'empty':
            empty()
    else:
        x = int(order[1])
        if order[0] == 'add':
            add(x)
        if order[0] == 'remove':
            remove(x)
        if order[0] == 'check':
            check(x)
        if order[0] == 'toggle':
            toggle(x)
        



'''
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
'''