import sys
input = sys.stdin.readline

N = int(input())   # 컴퓨터 수
M = int(input())   # 연결된 쌍 수

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
count = 0

def dfs(v):
    global count
    visited[v] = True

    for nxt in graph[v]:
        if not visited[nxt]:
            count += 1
            dfs(nxt)

dfs(1)
print(count)