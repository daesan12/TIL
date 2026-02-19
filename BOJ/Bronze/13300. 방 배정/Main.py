counting_arr = [[0]*2  for _ in range(7)]

#N학생수 K방 최대인원
N, K = map(int , input().split())

for _ in range(N):
    S, Y = map(int , input().split())
    counting_arr[Y][S] += 1

ans = 0
for y in range(1,7):
    for s in range(2):
        x = counting_arr[y][s]
        ans += x//K
        if x % K != 0:
            ans +=1

print(ans)
