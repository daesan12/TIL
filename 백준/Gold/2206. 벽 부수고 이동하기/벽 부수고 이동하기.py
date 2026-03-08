from collections import deque

def bfs(r,c):

    q.append((r,c,0))
    while q:

        r,c,broken = q.popleft()
        if r == R - 1 and c == C - 1:
            print(max(visited[0][r][c],visited[1][r][c]))
            exit()

        for i in range(4):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < R and 0 <= nj < C:#격자 범위 체크

                if broken == 1 and visited[1][ni][nj] == 0:#벽을 부쉈다면
                    if arr[ni][nj] == 1:#갈수없는 길이면
                        continue
                    else:#갈수있는 길이면
                        visited[1][ni][nj] = visited[1][r][c] + 1
                        q.append((ni,nj,1))
                elif broken == 0 and visited[0][ni][nj] == 0 and arr[ni][nj] == 0:#벽을 부수지않았다면
                #갈수있는 길이면
                    visited[0][ni][nj] = visited[0][r][c] + 1
                    q.append((ni, nj, 0))
                elif broken == 0 and visited[1][ni][nj] == 0 and arr[ni][nj] == 1:#갈수 없는길이면
                    visited[1][ni][nj] = visited[0][r][c] + 1
                    q.append((ni, nj, 1))
                        
    return

di = [0,1,0,-1]
dj = [1,0,-1,0]


R,C = map(int, input().split())
arr = [list(map(int, input()))for _ in range(R)]
visited = [[[0] * C for _ in range(R)]for _ in range(2)]
visited[0][0][0] = 1
q = deque()
bfs(0,0)
print(-1)