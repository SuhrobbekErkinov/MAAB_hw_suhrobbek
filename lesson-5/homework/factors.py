def print_factors(n):
    """Print all factors of a given number."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

def main():
    """Main function to get user input and find factors."""
    num = int(input("Enter a positive integer: "))
    print_factors(num)

if __name__ == "__main__":
    main()
