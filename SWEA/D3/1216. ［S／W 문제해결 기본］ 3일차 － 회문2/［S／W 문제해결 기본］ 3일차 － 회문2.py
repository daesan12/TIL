def is_pal(tmp):
    return tmp == tmp[::-1]

T = 10
N = 100
for test_case in range(1, T + 1):
    tc = input()
    data=[list(input().strip()) for _ in range(N)]

    ans = 0

    #길이 큰 것부터 내려가며 탐색
    for  L in range(N, 0, -1):
        found = False

        #가로 회문
        for row in range(N):
            tmp = ''
            for col in range(N - L +1):
                tmp = data[row][col:col+L]
                if is_pal(tmp):
                    ans = L
                    found = True
                    break
            if found:
                break
    
        #세로 회문(가로에서 못 찾았을 때만)
        if not found:
               #가로 회문
            for col in range(N):
                tmp = ''
                for row in range(N - L +1):
                    tmp = [data[row+i][col] for i in range(L)]
                    if is_pal(tmp):
                        ans = L
                        found = True
                        break
                if found:
                    break
        if found:
            break
    
    print(f"#{tc} {ans}")