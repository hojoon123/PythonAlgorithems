# 인구 수 / 가지고있는 돈 / 이벤트 리스트(문자열 원소)
def solution(p, money, events):
    global pay, event, result, visited, nums
    pay = []
    event = []
    buho = []
    nums = []
    result = []
    cur_money = 0
    score = 0
    visited = [0] * len(events)
    for item in events:
        pay.append(item.split()[0])
        event.append(item.split()[1])
    for i in event:
        buho.append(i[0])
        nums.append(i[1:])
    func(0, p, money)

    return max(result)


def func(cur_money, score, money):
    result.append(score)
    for i in range(len(pay)):
        if visited[i] == 0 and (cur_money + int(pay[i])) <= money:
            visited[i] = 1
            if event[i][0] == "+":
                func(cur_money + int(pay[i]), score + int(nums[i]), money)
            else:
                func(cur_money + int(pay[i]), score * int(nums[i]), money)
            visited[i] = 0
    return