a = int(input())
for i in range(a):
    cnt, b = input().split()
    for j in b:
        print(j * int(cnt), end = "")
    print()

'''
2
3 ABC
5 /HTP
출
AAABBBCCC
/////HHHHHTTTTTPPPPP
0부터 순차
'''