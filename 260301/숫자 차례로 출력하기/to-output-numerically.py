n = int(input())
def print_dawn(n):

    if n == 0:
        return 0
    print_dawn(n - 1)
    print(n,end=" ")

def print_up(n):
    if n == 0:
        return 0
    print(n,end=" ")
    print_up(n - 1)
print_dawn(n)
print()
print_up(n)

