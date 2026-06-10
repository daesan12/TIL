T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    
    arr = [list(map(int, input().split()))for _ in range(N)]
    max_score = 0
    for i in range(N):
        for j in range(N):
            score = 0
            if i+M <= N and j+M <= N:
                for k in range(i,i+M):
                    for l in range(j,j+M):
                        score += arr[k][l]
                if max_score < score:
                    max_score = score

    print(f"#{tc} {max_score}")