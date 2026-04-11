
from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]#우하좌상

def bfs(row,col,direction,k):
    d = deque()
    #(dir + 1) % 4 우
    #(dir + 3) % 4 좌
    d.append((row,col,direction,k,0))

    while d:
        row,col,direction,remain,cnt = d.popleft()
        if arr[row][col] == 'Y':
            return cnt

        #좌회전
        if visited[row][col][(direction+3)%4][remain] == 0:
            d.append((row,col,(direction+3)%4,remain,cnt +1))
            visited[row][col][(direction+3)%4][remain] = 1
        #우회전
        if visited[row][col][(direction + 1) % 4][remain] == 0:
            d.append((row, col, (direction+1)%4, remain, cnt +1))
            visited[row][col][(direction + 1) % 4][remain] = 1
        #전진
        ni = row + di[direction]
        nj = col + dj[direction]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 'T':
            if visited[ni][nj][direction][remain] == 0:
                visited[row][col][direction][remain] = 1
                d.append((ni,nj,direction,remain,cnt+1))

            #전진and 나무 만났을떄
        elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'T' and remain > 0:
            if visited[ni][nj][direction][remain-1] == 0:
                visited[row][col][direction][remain-1] = 1
                d.append((ni, nj, direction, remain-1, cnt + 1))



    return -1
T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[[[0] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    row,col = 0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                row = i
                col = j
    direction = 3
    visited[row][col][direction][K] = 1
    ans = bfs(row,col,direction,K)
    cnt = 0

    print(f"#{tc} {ans}")