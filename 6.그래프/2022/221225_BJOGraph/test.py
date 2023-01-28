from sys import stdin
input = stdin.readline

while 1:
    tri = list(map(int,input().split()))
    max_num = max(tri)
    if tri == [0,0,0]: exit()
    tri.remove(max_num)
    if tri[0] ** 2 + tri[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')

'''
3, 4, 5
'''