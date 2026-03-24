def dfs(player,score):
    global max_score
    if player == 11:
        max_score = max(max_score,score)
        return 
    
    for i in range(11):
        if arr[player][i] == 0 or used[i] == True:
            continue
        used[i] = True
        dfs(player+1,arr[player][i]+score)
        used[i] = False

T = int(input())
for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    used= [False] * 11
    max_score = 0
    dfs(0,0)
    print(max_score)