X, Y = map(int, input().split())
arr = [[0] * X for _ in range(Y)]
N = int(input())
cut_arr = [list(map(int,input().split())) for _ in range(N)]
horizontal = [0, X] #가로값
vertical = [0, Y] #세로값 
#가로 0 세로 1

for cut in cut_arr:
    #가로
    if cut[0] == 0:
        vertical.append(cut[1])
    elif cut[0] == 1:
        horizontal.append(cut[1])

horizontal.sort()
vertical.sort()

max_horizontal = 0
max_vertical = 0

for i in range(0,len(horizontal)-1):
    if horizontal[i+1] - horizontal[i] > max_horizontal:
        max_horizontal = horizontal[i+1] - horizontal[i]

for i in range(0,len(vertical)-1):
    if vertical[i+1] - vertical[i] > max_vertical:
        max_vertical = vertical[i+1] - vertical[i]

print(max_horizontal * max_vertical)