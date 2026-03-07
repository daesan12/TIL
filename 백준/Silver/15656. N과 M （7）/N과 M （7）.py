def dfs():
    if len(s) == M:
        print(*s)
        return
    
    for i in range(N):
        if visited[i] == 0:
            s.append(arr[i])
            visited[i] == 1
            dfs()
            visited[i]==0
            s.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
arr.sort()
s = []
dfs()