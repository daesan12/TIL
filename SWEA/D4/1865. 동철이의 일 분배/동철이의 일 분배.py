def dfs(prob):
    global ans
    if prob <= ans:
        return
    if len(t) == N:
        sum = 1.0
        for i in range(N):
            sum *= t[i]
            if sum < ans :
                return
        ans = max(ans,sum)
        return
    
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1 
        t.append(arr[len(t)][i] / 100)
        dfs(prob * (arr[len(t)-1][i] / 100))
        visited[i] = 0
        t.pop()

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0.0
    visited = [0]*N
    t = []
    dfs(1.0)
    ans *= 100
    print(f"#{tc} {ans:.6f}")