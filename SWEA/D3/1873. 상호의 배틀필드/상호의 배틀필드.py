di = [0,1,0,-1]
dj = [1,0,-1,0]
T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())

    arr = [list(input()) for _ in range(H)]

    N = int(input())
    command = input()
    row, col = 0,0
    direction = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] in ('>','v','<','^'):
                if arr[i][j] == '>':
                    row, col = i, j
                    direction = 0
                elif arr[i][j] == 'v':
                    row, col = i, j
                    direction = 1
                elif arr[i][j] == '<':
                    row, col = i, j
                    direction = 2
                elif arr[i][j] == '^':
                    row, col = i, j
                    direction = 3

    for i in range(N):
        if command[i] == 'R':
            arr[row][col] = '>'
            direction = 0
            if W > col + 1 and arr[row][col+1] == '.':
               arr[row][col] = '.'
               col += 1
               arr[row][col] = '>'
        elif command[i] == 'D':
            arr[row][col] = 'v'
            direction = 1
            if H > row + 1 and arr[row+1][col] == '.':
               arr[row][col] = '.'
               row += 1
               arr[row][col] = 'v'
        elif command[i] == 'L':
            arr[row][col] = '<'
            direction = 2
            if 0 <= col - 1 and arr[row][col-1] == '.':
               arr[row][col] = '.'
               col -= 1
               arr[row][col] = '<'
        elif command[i] == 'U':
            arr[row][col] = '^'
            direction = 3
            if 0 <= row - 1 and arr[row-1][col] == '.':
               arr[row][col] = '.'
               row -= 1
               arr[row][col] = '^'
        elif command[i] == 'S':
            a = max(W,H)
            for step in range(1,a+1):
                ni = row + di[direction] * step
                nj = col + dj[direction] * step
                if 0 <= ni < H and 0 <= nj < W:
                    if arr[ni][nj] =='*':
                        arr[ni][nj] = '.'
                        break
                    elif arr[ni][nj] == '#':
                        break
    print(f"#{tc}",end = ' ')
    for i in range(H):

        print(''.join(arr[i]))