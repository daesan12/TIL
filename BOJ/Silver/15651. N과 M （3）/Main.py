def dfs(depth,arr):

    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        visited[i] = 1
        dfs(depth +1 ,arr)
        visited[i] = 0
        arr.pop()
    

N, M = map(int, input().split())
arr = []
visited = [0] * (N +1)
dfs(0,arr)