from collections import deque

N, K = map(int, input().split())

MAX = 100001
visited = [False] * MAX

q = deque()
q.append((N, 0))  # 위치, 시간
visited[N] = True

while q:
    x, t = q.popleft()

    if x == K:
        print(t)
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx < MAX and not visited[nx]:
            visited[nx] = True
            q.append((nx, t+1))