MOD = 998244353

def sum_1_to_n(n):
    return (n % MOD) * ((n + 1) % MOD) * pow(2, MOD - 2, MOD) % MOD

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    ans = sum_1_to_n(a)
    ans = ans * sum_1_to_n(b) % MOD
    ans = ans * sum_1_to_n(c) % MOD

    print(ans)