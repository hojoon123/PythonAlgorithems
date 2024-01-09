import sys
input = sys.stdin.readline

def solve(n, k):
    ans = 0

    if n > k:
        ans += k * (n - k)
        n = k

    d = []
    for i in range(1, k):
        if i * i > k:
            break
        if k % i == 0:
            d.append(i)
            if k // i != i:
                d.append(k // i)

    d = list(set(d))

    def sum_range(l, r):
        return (r + l) * (r - l + 1) // 2

    def get_ans(l, r, x):
        hi = d.index(r) + 1 if r in d else len(d)
        lo = d.index(l) if l in d else 0

        ret = (r - l + 1) * k - sum_range(l, r) * x

        for i in range(lo, hi):
            ret -= k - x * d[i]

        return ret

    r = min(k, n)
    while r > 0:
        if k % r == 0:
            r -= 1
            continue

        x = k // r
        l = k // (x + 1) + 1

        if l <= r:
            ans += get_ans(l, r, x)

        r = min(l, r) - 1

    print(ans)
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)