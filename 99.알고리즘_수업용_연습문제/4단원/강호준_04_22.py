import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 분할
def find_fake_coin(coins):
    group_size = len(coins) // 3
    # 그루핑
    group1 = coins[:group_size]
    group2 = coins[group_size:2 * group_size]
    group3 = coins[2 * group_size:]

    # 두 그룹을 양팔저울에 올려서 비교합니다.
    result = weigh(group1, group2)

    # 3번 그룹에 위조 동전
    if result == 0:
        fake_coin = find_fake_in_group3(group3, group1)
    # 1번 혹은 2번 그룹에 위조 동전
    else:
        if result == -1:
            light_group = group1
            heavy_group = group2
        else:
            light_group = group2
            heavy_group = group1
        normal_group = group3
        fake_coin = find_fake_in_group12(light_group, heavy_group, normal_group)

    return fake_coin
    

# 정복 1번 혹은 2번 그룹에 있을 경우
def find_fake_in_group12(light_group, heavy_group, normal_group):
    # light 그룹을 기준으로 비교 가벼운 곳 3개 heavy 1개
    # 정상 3개 light 그룹 1개
    sub_group_size = 3
    sub_group1 = light_group[:sub_group_size] + [heavy_group[-1]]
    sub_group2 = normal_group[:sub_group_size] + [light_group[-1]]
    result = weigh(sub_group1, sub_group2)
    
    # 덜어낸 heavy그룹 3개 중 위조 동전
    if result == 0:
        return last_weigh(heavy_group, result)

    # light 그룹이 3개가 들어간 곳이 무겁다면
    # 올려둔 heavy 그룹 1개 or 정상그룹에 넣어둔 light 그룹 1개가 위조 동전
    elif result == 1:
        if heavy_group[-1][0] > normal_group[-1][0] or heavy_group[-1][0] < normal_group[-1][0]:
            return heavy_group[-1]
        elif heavy_group[-1][0] == normal_group[-1][0]:
            return light_group[-1]
    
    # 정상동전 3개가 들어간 곳이 무겁다면
    # light 그룹 3개 중 위조 동전 포함
    else:
        return last_weigh(light_group, result)

# 정복 3번째 그룹에 있을 경우 2-2의 방식
def find_fake_in_group3(dummy_group, normal_group):
    # 정상인 1번 그룹에서 3개 위조 동전이 있는 3번 그룹에서 3개
    sub_group_size = 3
    dummys = dummy_group[:sub_group_size]
    normals = normal_group[:sub_group_size]

    # 두 부분 그룹을 비교
    result = weigh(dummys, normals)

    # 무게가 같을 경우
    if result == 0:
        # 3번그룹에서 나머지 1개가 위조 동전
        return dummy_group[-1]
    
    # 무게가 다를 경우
    else:
        return last_weigh(dummy_group, result)

# 무게 구현
def weigh(coins1, coins2):
    # 반환값이 0이면 무게가 같음
    # 1이면 coins1이 더 무거움
    # -1이면 coins2가 더 무거움
    total_weight_coins1 = sum(coin[0] for coin in coins1)
    total_weight_coins2 = sum(coin[0] for coin in coins2)

    if total_weight_coins1 == total_weight_coins2:
        return 0
    elif total_weight_coins1 > total_weight_coins2:
        return 1
    else:
        return -1
    

# 마지막 비교
def last_weigh(group, result):
    total_weight_coins1 = group[0][0]
    total_weight_coins2 = group[1][0]

    if total_weight_coins1 == total_weight_coins2:
        ans = 0
    elif total_weight_coins1 > total_weight_coins2:
        ans = 1
    else:
        ans = -1
        
    if ans == 0:
        return group[2]
    elif (result == 1 and ans == 1) or (result == -1 and ans == -1):
        return group[0]
    elif (result == 1 and ans == -1) or (result == -1 and ans == 1):
        return group[1]
        
if __name__ == "__main__":
    coins_list = [(10,"정상") for i in range(11)]
    coins_list.insert(6,(9,"위조"))
    print(coins_list) 
    fake_coin = find_fake_coin(coins_list)
    print("위조 동전:", fake_coin)