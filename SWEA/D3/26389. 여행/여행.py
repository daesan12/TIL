T = int(input())

for _ in range(T):
    A = input().strip()

    n = A.count('N')
    s = A.count('S')
    e = A.count('E')
    w = A.count('W')

    possible = True

    # 세로축: N만 있거나 S만 있으면 원점 복귀 불가능
    if (n > 0 and s == 0) or (s > 0 and n == 0):
        possible = False

    # 가로축: E만 있거나 W만 있으면 원점 복귀 불가능
    if (e > 0 and w == 0) or (w > 0 and e == 0):
        possible = False

    print("Yes" if possible else "No")