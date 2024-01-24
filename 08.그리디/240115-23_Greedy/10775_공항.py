import sys
input = sys.stdin.readline

def find_root(airplane):
    stack = [airplane]

    while True:
        parking_gate = alters[airplane]

        if parking_gate == airplane:
            break
        else:
            stack.append(parking_gate)
            airplane = alters[parking_gate]

    while stack:
        temp = stack.pop()
        alters[temp] = parking_gate

    return parking_gate

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)

    alters[a_root] = b_root

if __name__ == "__main__":
    num_gates = int(input())
    num_airplanes = int(input())
    airplanes = [int(input()) for _ in range(num_airplanes)]
    alters = list(range(num_gates+1))
    cnt = 0

    for i in range(num_airplanes):
        airplane = airplanes[i]
        root = find_root(airplane)

        if root == 0:
            break

        union(root, root-1)
        cnt += 1

    print(cnt)