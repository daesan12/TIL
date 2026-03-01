def start_find(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def bfs(i,j):
    que = []
    que.append((i,j))
    while que:
        i,j = que.pop(0)
        if arr[i][j] == 3:
            return visited[i][j] - 1 
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    que.append((ni,nj))
                    visited[ni][nj] += visited[i][j] + 1
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input()))for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start_i, start_j =  start_find(N)
    result = bfs(start_i, start_j)
    if result is None:
        result = 0
    print(f"#{tc} {result}")