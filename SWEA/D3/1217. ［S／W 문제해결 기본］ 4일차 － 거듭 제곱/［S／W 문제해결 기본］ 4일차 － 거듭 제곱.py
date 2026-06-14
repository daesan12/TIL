def dfs(n,m):
    global M
    global tc
    if m == M:
        print(f"#{tc} {n}")
        return 
    dfs(n*N, m+1)

for _ in range(10):
    tc = int(input())
    N,M = map(int,input().split())
    
    answer = dfs(N,1)