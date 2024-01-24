import sys

arr = []
while 1:
    try:
        arr.append(str(input()))
    except:
        break
print('\n'.join(arr))
