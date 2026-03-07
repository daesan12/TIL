import sys
def dfs(start):
    
    if len(s) == M:
        print(*s)
        return
    for i in range(N):
        if visited[i] == 0:
            s.append(arr[i])
            visited[i] = 1
            dfs(i)
            s.pop()
            visited[i] = 0
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited= [0] * N
s = []
dfs(0)