N = int(input())
# 개수를 받는다
arr = []
# 3
# happy
# abccba
# new 
# 2 떠야함
for i in range(N):
    arr.append(list(input()))
for j in range(N):
    for k in range(len(arr[j])-1):
        countnumber = arr[j].count(arr[j][k])
        flat = False
        if countnumber > 1:
            if (k < len(arr[j]) - 1 and arr[j][k] == arr[j][k + 1]) or (k > 0 and arr[j][k] == arr[j][k - 1]) or len(
                    arr[j]) == 1:

            else:
                arr[j] = 0
                break

count = arr.count(0)
for z in range(count):
    arr.remove(0)
print(len(arr))           
