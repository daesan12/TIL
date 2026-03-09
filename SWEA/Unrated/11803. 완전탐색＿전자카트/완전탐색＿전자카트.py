def dfs():
    global max_sum
    if len(arr) == N:

        arr.append(0)
        #print(*arr)
        sum = 0
        for i in range(len(arr)-1):
            sum += cost[arr[i]][arr[i+1]]
        if sum < max_sum:
            max_sum = sum
        arr.pop()
        return
    
    for i in range(1,N):
        
        if visited[i] == 1:
            continue
        arr.append(i)
        visited[i] = 1
        dfs()
        arr.pop()
        visited[i] = 0
    return max_sum
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    arr = [0]
    visited = [0] * N
    max_sum= 9999999999
    print(f"#{tc} {dfs()}")