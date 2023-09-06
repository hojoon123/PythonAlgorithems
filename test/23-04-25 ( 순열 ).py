import copy
import sys
input = sys.stdin.readline

result = []                                 # a => join 함수 안에서 list1과 list2를 조합해 result에 추가하기 위한 리스트  /  result => 조합된 리스트
list = list(map(int,input().split()))       #  입력 받은 숫자 리스트에 넣기


# 이후 2, 3, 4는 join으로 하나씩 증가
def join(list1,list2):          # list1 => list / list2 => result   --> 33번줄에서 함수 호출(list,result)
    result,ab = [],[]
    list_copy = copy.deepcopy(list1)
    result_copy = copy.deepcopy(list2)

    for i in list_copy:
        for j in range(len(result_copy)):
            if i not in result_copy[j]:
                ab.append(i)
                ab.extend(result_copy[j])
                result.append(ab)
                ab = []
    return result

# 처음에 1번은 setData로 사용
def setData(list1,list2):
    a = []
    for j in list:
        for k in list:
            if j != k:
                a.append(j)
                a.append(k)
                result.append(a)
                a = []
    return result


# 본문 내용
for i in range(len(list) - 1):
    if result:
        result = join(list,result)
    else:
        result = setData(list, result)

print(result)