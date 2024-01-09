n = int(input())
flag_a = [0] * n
flag_b = [0] * (2 * n - 1)
flag_c = [0] * (2 * n - 1)
count = 0

def recursive(i):
    global count

    if i == n:
        count += 1
        return

    for j in range(n // 2 if i == 0 else n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n - 1]:
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = 1
            recursive(i + 1)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = 0

# 가장 첫번째 열 둘때 행을 절반만 시행하기 때문에 2배
recursive(0)
count *= 2

# 홀수면 첫번째 열 둘때 중간 행을 시행하지 않았기 때문에
# 첫번째열 중간 행에 두었다 하고 다음 열부터 시행
if n % 2 != 0:
    flag_a[n // 2] = flag_b[n // 2] = flag_c[n // 2] = 1
    recursive(1)

print(count)