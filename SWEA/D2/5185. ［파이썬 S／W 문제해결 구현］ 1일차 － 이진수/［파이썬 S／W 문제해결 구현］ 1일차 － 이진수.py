T = int(input())
for tc in range(1,T+1):
    N, HEX = input().split()
    t = ''
    N = int(N)    
    for i in range(N):
        t += ''.join(bin(int(HEX[i], 16))[2:]).zfill(4)
    print(f"#{tc} {t}")