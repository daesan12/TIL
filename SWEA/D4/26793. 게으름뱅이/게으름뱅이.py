TC = int(input())

for _ in range(TC):
    N = int(input())
    works = []

    for _ in range(N):
        duration, deadline = map(int, input().split())
        works.append((deadline, duration))

    works.sort(reverse=True)

    now = 10**18

    for deadline, duration in works:
        now = min(now, deadline)
        now -= duration

    print(now)