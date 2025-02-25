def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

def test2():
    n = int(input("Enter an integer value: "))
    print_squares(n)
if __name__ == '__main__':
    test2()