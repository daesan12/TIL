T = int(input())
for tc in range(1,T+1):
    N, K = map(int, (input().split()))
    arr = [i for i in range(0,13)]
    count = 0

    for mask in range(1<<12):
        cnt = 0
        total = 0
        for i in range(12):
            if mask & (1<<i):
                cnt += 1
                total += (i+1)
        if cnt == N and total == K:
            count += 1
    print(f"#{tc} {count}")
