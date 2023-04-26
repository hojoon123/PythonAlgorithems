import sys
input = sys.stdin.readline


def func(key):
    global my_data_list
    key_list = []
    ans = []
    l_list = len(my_data_list)
    for i in range(l_list):
        key_list.append(my_data_list[i][key])
    key_list.sort()
    for i in range(l_list):
        for j in range(l_list):
            if key_list[i] == my_data_list[j][key]:
                ans.append(my_data_list.pop(j))
                break
    return ans

if __name__ == '__main__':
    my_data_list = [[1, 2], [2, 1], [3, 5], [4, 4], [6, 3]]
    print(func(1))
    
'''
my_data_list = sorted(my_data_list, key=lambda x: x[1])
'''