word = input()
cnt = [0] * 26

for ch in word:
    cnt[ord(ch) - ord('a')] += 1

print(*cnt)