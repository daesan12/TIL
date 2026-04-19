from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    visited = [[-1] * M for _ in range(N)]
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 0
    max_dist = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 'L' and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    max_dist = max(max_dist, visited[nr][nc])
                    q.append((nr, nc))

    return max_dist

answer = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)