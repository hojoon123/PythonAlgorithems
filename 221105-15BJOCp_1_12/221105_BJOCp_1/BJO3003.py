inItems = list(map(int,input().split()))
piece =[1,1,2,2,2,8]

for i in range(6):
    print(piece[i]-inItems[i], end=" ")

# 6개
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개