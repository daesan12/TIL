from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]#우하좌상
pipe = [[] for i in range(8)]
pipe[1] = [0,1,2,3]#우하좌상
pipe[2] = [1,3]#하,상
pipe[3] = [0,2]#좌,우
pipe[4] = [0,3]#우,상
pipe[5] = [0,1]#우,하
pipe[6] = [1,2]#하,좌
pipe[7] = [2,3]#좌,상
def bfs(row,col):
    d = deque()
    d.append((row,col,1))
    global L

    while d:
        i,j,time = d.popleft()
        if time == L:
           continue
        for direction in pipe[arr[i][j]]:
            ni = i + di[direction]
            nj = j + dj[direction]
            if 0 <= ni < N and 0 <= nj < M and (direction + 2) % 4 in pipe[arr[ni][nj]]:
                if visited[ni][nj] == 0:
                    d.append((ni,nj,time+1))
                    visited[ni][nj] = 1


T = int(input())

for tc in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    bfs(R,C)
    cnt = 0
    for i in range(N):
        cnt += visited[i].count(1)
    print(f"#{tc} {cnt}")