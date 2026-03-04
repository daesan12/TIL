def  dfs(depth,arr):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        if visited[i] ==1:
            continue
        arr.append(i)
        visited[i] =1 
        depth += 1
        dfs(depth,arr)
        depth -= 1
        visited[i] =0 
        arr.pop()



arr = []
N, M = map(int,input().split())
visited = [0]*(N+1)
dfs(0,arr)