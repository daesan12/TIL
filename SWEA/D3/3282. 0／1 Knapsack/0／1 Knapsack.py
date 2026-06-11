T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    dp = [0] * (K + 1)

    for _ in range(N):
        V, C = map(int, input().split())

        for w in range(K, V - 1, -1):
            dp[w] = max(dp[w], dp[w - V] + C)
    print(f'#{tc} {dp[K]}')