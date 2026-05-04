
def count_ways(N, s):
    if 2 <= s <= N + 1:
        return s - 1
    elif N + 1 < s <= 2 * N:
        return 2 * N - s + 1
    return 0

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    result = 0

    # y = c+d
    for y in range(2, 2 * N + 1):
        x = y + K  # a+b

        if 2 <= x <= 2 * N:
            result += count_ways(N, y) * count_ways(N, x)

    print(result)