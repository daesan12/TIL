#중복가능한 오름차순 수열
def dfs(start):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(start,N):
        s.append(arr[i])
        dfs(i)
        s.pop()        

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs(0)