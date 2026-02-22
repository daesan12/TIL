from collections import deque

n = int(input())
cmd = []
dq = deque()

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_back"]:
        dq.append(int(line[1]))
    elif line[0] in ["push_front"]:
        dq.appendleft(int(line[1]))
    elif line[0] in ["pop_front"]:
        print(dq.popleft())
    elif line[0] in ["pop_back"]:
        print(dq.pop())
    elif line[0] in ["size"]:
        print(len(dq))
    elif line[0] in ["empty"]:
        if dq:
            print(0)
        else:
            print(1)
    elif line[0] in ["front"]:
        print(dq[0])
    elif line[0] in ["back"]:
        print(dq[-1])

