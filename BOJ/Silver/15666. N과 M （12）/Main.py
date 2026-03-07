def dfs(start):

    if len(s) == M:
        print(*s)
        return
    prev = None
    for i in range(start,N):
        if prev == arr[i]:
            continue
        prev = arr[i]
        s.append(arr[i])
        dfs(i)
        s.pop()       

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs(0)