def dfs(start):

    if len(s) == M:
        print(*s)
        return
    prev = None
    for i in range(start,N):
        if prev == arr[i]:
            continue

        s.append(arr[i])
        prev = arr[i]
        dfs(i+1)
        s.pop()        


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs(0)