def dfs(idx,n_len,n_sum):
    global ans
    if n_len > N or n_sum > K:
        return
    if n_len == N and n_sum == K:
        ans += 1
        return

    for i in range(idx,13):
        dfs(i+1, n_len+1,n_sum +i)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    ans = 0
    t = []
    dfs(1,0,0)
    print(f"#{tc} {ans}")
    