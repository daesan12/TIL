n = int(input())

def print_hello(n):
    if n == 0:
        return 0
    print_hello(n-1)
    print("HelloWorld")
print_hello(n)