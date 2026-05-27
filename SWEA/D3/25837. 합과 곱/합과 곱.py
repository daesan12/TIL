T = int(input())

for _ in range(T):
    S, P = map(int, input().split())

    D = S * S - 4 * P

    if D < 0:
        print("No")
        continue

    sqrtD = int(D ** 0.5)

    if sqrtD * sqrtD != D:
        print("No")
        continue

    if (S + sqrtD) % 2 == 0 and (S - sqrtD) % 2 == 0:
        print("Yes")
    else:
        print("No")