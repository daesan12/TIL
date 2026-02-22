N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    elif line[0] == "pop":
        print(A.pop(0))
    elif line[0] == "size":
        print(len(A))
    elif line[0] == "empty":
        if len(A) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == "front":
        print(A[0])