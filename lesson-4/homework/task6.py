def print_primes():
    for num in range(2, 101):
        is_prime = all(num%i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            print(num, end=' ')

if __name__ == '__main__':
    print_primes()