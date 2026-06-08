T= int(input())

for tc in range(1,T+1):

    N = int(input())
    speed = 0
    distance = 0

    for _ in range(N):
        command = list(map(int, input().split()))

        if command[0] == 1:
            #가속
            speed += command[1]
        elif command[0] == 2:
            #감속
            speed -= command[1]
        
        if speed < 0:
            speed = 0

        distance += speed
            
    print(f"#{tc} {distance}")

