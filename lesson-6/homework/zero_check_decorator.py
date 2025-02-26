def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

if __name__ == "__main__":
    a = int(input("Enter an integer value for a: "))
    b = int(input("Enter an integer value for b: "))
    print(div(a, b))