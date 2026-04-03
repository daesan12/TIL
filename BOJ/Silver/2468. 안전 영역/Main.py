from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(row,col):
    d = deque()
    d.append((row,col))
    while d:
        i,j = d.popleft()
        for step in range(4):
            ni = i + di[step]
            nj = j + dj[step]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                d.append((ni,nj))
                visited[ni][nj] = 1

 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

point_arr = [[0] * N for _ in range(N)]
max_h = 0
max_count = 0
for i in range(N):
    h = max(arr[i])
    max_h = max(max_h,h)

for rain in range(0,max_h):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                visited[i][j] = 1
                
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i,j)
                count += 1
    max_count = max(max_count,count)

print(max_count)