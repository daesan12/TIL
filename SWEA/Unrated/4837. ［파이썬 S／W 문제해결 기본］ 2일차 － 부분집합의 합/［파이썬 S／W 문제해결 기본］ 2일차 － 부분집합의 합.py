def dfs(start):
    global count
    if len(s) == N and sum(s) == K:
         count += 1
         return 
    if len(s) > N or sum(s) > K:
        return
    
    for i in range(start,13):
        if sum(s) + arr[i] > K:
            break
        s.append(i)
        dfs(i+1)
        s.pop()
       

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int,input().split()))
    arr = [i for i in range(13)]
    s = []
    count = 0
    
    dfs(1)
    print(f"#{tc} {count}")