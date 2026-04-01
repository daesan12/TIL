from collections import deque

def bfs():
    global ans
    d = deque()
    d.append(1)

    while d:

        idx = d.popleft()
        for i in node[idx]:
            if visited[i] == 1:
                continue

            visited[i] = 1
            ans += 1
            d.append(i)

    return visited.count(1) -1

N = int(input())
C = int(input())
arr = [list(map(int, input().split())) for _ in range(C)]
node = [[] for _ in range(N+1)]

for i in range(C):
    node[arr[i][0]].append(arr[i][1])
    node[arr[i][1]].append(arr[i][0])
visited = [0] * (N+1)
visited[1] = 1
ans = 0
bfs()

print(ans)