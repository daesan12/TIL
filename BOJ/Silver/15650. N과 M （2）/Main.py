def dfs(depth,arr):
    if depth == M:
        print(*arr)

    for i in range(1,N+1):
        if visited[i] == 1:
            continue
        if len(arr) >=  1:
            if arr[depth-1] >= i:
                continue

        arr.append(i)
        visited[i] = 1
        dfs(depth + 1,arr)
        visited[i] = 0
        arr.pop()

N,M = map(int,input().split())
arr = []
visited= [0] * (N+1)
dfs(0,arr)    
