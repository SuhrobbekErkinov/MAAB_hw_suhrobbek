def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

if __name__ == '__main__':
    n = int(input("Enter an integer value: "))
    print_squares(n)