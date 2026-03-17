import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx,ny)


T = int(input())

for _ in range(T):

    M,N,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        arr[y][x] = 1

    worm = 0

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1 and not visited[y][x]:
                dfs(x,y)
                worm += 1

    print(worm)