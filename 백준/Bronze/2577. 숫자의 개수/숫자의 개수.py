a = int(input())
b = int(input())
c = int(input())

num = a * b * c
count = [0] * 10

for ch in str(num):
    count[int(ch)] += 1

for i in range(10):
    print(count[i])