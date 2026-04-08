s = input()
result = ''

for ch in s:
    if 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
    else:
        result += ch

print(result)