N = int(input())

T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N):
    # i번째 날 상담을 안 하는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])

    # i번째 날 상담을 하는 경우
    end = i + T[i]
    if end <= N:
        dp[end] = max(dp[end], dp[i] + P[i])

print(dp[N])