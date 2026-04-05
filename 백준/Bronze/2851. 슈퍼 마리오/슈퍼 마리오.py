import sys

scores = [int(sys.stdin.readline()) for _ in range(10)]

total = 0

for score in scores:
    total += score
    if total >= 100:
        before = total - score
        if abs(100 - before) < abs(100 - total):
            print(before)
        else:
            print(total)
        break
else:
    print(total)