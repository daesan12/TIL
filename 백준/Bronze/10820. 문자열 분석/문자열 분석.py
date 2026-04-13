while True:
    try:
        s = input()

        lower = 0
        upper = 0
        digit = 0
        space = 0

        for ch in s:
            if ch.islower():
                lower += 1
            elif ch.isupper():
                upper += 1
            elif ch.isdigit():
                digit += 1
            elif ch == ' ':
                space += 1

        print(lower, upper, digit, space)

    except EOFError:
        break