N, M = map(int, input().split())

arr = []

def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for num in range(start, N + 1):
        arr.append(num)
        dfs(num)          # 같은 수 또 선택 가능
        arr.pop()

dfs(1)