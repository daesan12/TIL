from collections import deque

di = [-2,-1,1,2,2,1,-1,-2]
dj = [1,2,2,1,-1,-2,-2,-1]

def bfs(row,col):
    visited[row][col] = 1
    d = deque()
    d.append((row,col,0))
    cnt = 0
    while d:
        r,c,dep = d.popleft()
        if r == GOAL_ROW and c == GOAL_COL:
            return dep
        
        for i in range(8):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    d.append((ni,nj,dep+1))

T = int(input())
for tc in range(T):
    N = int(input())
    knight_row, knight_col = map(int ,input().split())
    GOAL_ROW, GOAL_COL = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    ans = bfs(knight_row,knight_col)
    print(ans)