T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    A = (X + Y) // 2
    B = (X - Y) // 2

    print(A, B)