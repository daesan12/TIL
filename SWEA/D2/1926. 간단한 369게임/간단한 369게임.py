N = int(input())

result = []

for i in range(1, N + 1):
    clap = 0
    
    for ch in str(i):
        if ch in '369':
            clap += 1
    
    if clap > 0:
        result.append('-' * clap)
    else:
        result.append(str(i))

print(*result)