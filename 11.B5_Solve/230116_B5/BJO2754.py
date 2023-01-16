from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    s = str(input().rstrip())
    arr = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,

            'B+': 3.3, 'B0': 3.0, 'B-': 2.7,

            'C+': 2.3, 'C0': 2.0, 'C-': 1.7,

            'D+': 1.3, 'D0': 1.0, 'D-': 0.7,

            'F': 0.0}
    print(arr[s])
'''
A+: 4.3, A0: 4.0, A-: 3.7

B+: 3.3, B0: 3.0, B-: 2.7

C+: 2.3, C0: 2.0, C-: 1.7

D+: 1.3, D0: 1.0, D-: 0.7

F: 0.0
예제 입력 1 
A0
예제 출력 1 
4.0
'''