from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

# 처음부터 익은 토마토 위치 전부 큐에 넣기
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while queue:
    r, c = queue.popleft()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            queue.append((nr, nc))

answer = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:   # 끝까지 안 익은 토마토가 있으면 실패
            print(-1)
            sys.exit()
        answer = max(answer, box[i][j])

# 처음 익은 토마토가 1부터 시작했으니까 -1
print(answer - 1)