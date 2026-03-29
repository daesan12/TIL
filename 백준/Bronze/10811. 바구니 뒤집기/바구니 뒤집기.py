N, M = map(int, input().split())

baskets = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)