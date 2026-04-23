from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 섬 번호 붙이기
island_id = 2  # 기존 0,1과 구분하려고 2부터 시작
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            q = deque()
            q.append((r, c))
            graph[r][c] = island_id

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dr[d]
                    ny = y + dc[d]

                    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                        graph[nx][ny] = island_id
                        q.append((nx, ny))

            island_id += 1

# 2. 모든 섬의 좌표를 시작점으로 넣는 멀티소스 BFS 준비
owner = [[0] * N for _ in range(N)]   # 어떤 섬에서 왔는지
dist = [[-1] * N for _ in range(N)]   # 바다 확장 거리
q = deque()

for r in range(N):
    for c in range(N):
        if graph[r][c] >= 2:
            owner[r][c] = graph[r][c]
            dist[r][c] = 0
            q.append((r, c))

# 3. 바다로 동시에 확장하면서 다른 섬과 만나는 최소 거리 찾기
answer = float('inf')

while q:
    x, y = q.popleft()

    for d in range(4):
        nx = x + dr[d]
        ny = y + dc[d]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        # 아직 방문 안 한 바다라면 현재 섬이 차지
        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            owner[nx][ny] = owner[x][y]
            q.append((nx, ny))

        # 이미 다른 섬이 차지한 칸이면 다리 길이 후보
        elif owner[nx][ny] != owner[x][y]:
            answer = min(answer, dist[nx][ny] + dist[x][y])

print(answer)