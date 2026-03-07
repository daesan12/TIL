import sys
def dfs(start):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(start,N):
        if visited[i] == 0:
            s.append(arr[i])
            visited[i] == 1
            dfs(i+1)
            visited[i]==0
            s.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
arr.sort()
s = []
dfs(0)