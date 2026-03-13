T = int(input())

for tc in range(1,T+1):
    ans = 0
    N = int(input())
    line = []
    for i in range(N):
        start , end = map(int, input().split())
        line.append((start,end))
        for j in range(len(line)):
            if start < line[j][0] and end > line[j][1]:
                ans += 1
            if start > line[j][0] and end < line[j][1]:
                ans += 1

    print(f"#{tc} {ans}")
    