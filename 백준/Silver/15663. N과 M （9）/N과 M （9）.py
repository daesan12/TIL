def dfs():

    if len(s) == M:
        print(*s)
        return
    prev = 0
    for i in range(N):
        if visited[i]:
            continue
        if prev == arr[i]:
            continue
        visited[i] = 1
        s.append(arr[i])
        prev = arr[i]
        dfs()
        visited[i] = 0
        s.pop()        


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]* N
s = []
dfs()