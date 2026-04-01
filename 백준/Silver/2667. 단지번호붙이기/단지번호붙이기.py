from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(num,row,col):
    d = deque()
    d.append((row,col))
    count = 1
    while d:
        r,c = d.popleft()
        for i in range(4):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = num
                d.append((ni,nj))
                count += 1

    return count

N = int(input())
arr = [list(map(int, input()))for _ in range(N)]
visited = [[0] * N for _ in range(N)]
num = 1
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1 
            cnt = bfs(num,i,j)
            ans.append(cnt)
            num += 1
print(num-1)
ans.sort()
for i in ans:
    print(i)
# for i in range(N):
#     print(visited[i])
