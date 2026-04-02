from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(row,col):
    global point
    global visited
    count = 1
    d = deque()
    d.append((row,col))

    while d:
        i,j = d.popleft()
        for step in range(4):
            ni = i + di[step]
            nj = j + dj[step]
            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0:
                d.append((ni,nj))
                visited[ni][nj] = point
                count += 1

    return count

M, N, K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
visited = [[0] * N for _ in range(M)]
point = 1
#도형칠하기
for start_col, start_row, end_col, end_row in arr:
    for i in range(start_row,end_row):
        for j in range(start_col, end_col):
            visited[i][j] = -1

ans = []
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = point
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')