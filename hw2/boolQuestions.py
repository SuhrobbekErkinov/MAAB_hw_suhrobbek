def prob1():
    print("---Problem 1---")
    username = input("Enter an username: ")
    password = input("Enter a password: ")
    if username and password:
        return True
    else:
        return False

def prob2():
    print("---Problem 2---")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    return num1 == num2

def prob3():
    print("---Problem 3---")
    num = int(input("Enter a number: "))
    return num>0 and num%2 == 0

def prob4():
    print("---Problem 4---")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    num3 = float(input("Enter 3rd number: "))
    return num1 != num2 and num2 != num3 and num1 != num3

def prob5():
    print("---Problem 5---")
    st1 = input("Enter the 1st string: ")
    st2 = input("Enter the 2nd string: ")
    return len(st1) == len(st2)

def prob6():
    print("---Problem 6---")
    num = int(input("Enter an integer: "))
    return num%3 == 0 and num%5 == 0

def prob7():
    print("---Problem 7---")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    return num1 + num2 > 50.8

def prob8():
    print("---Problem 8---")
    num = float(input("Enter a number: "))
    return 10 <= num <= 20

def main3():
    print("Boolean Type Questions: ")
    print(prob1())
    print(prob2())
    print(prob3())
    print(prob4())
    print(prob5())
    print(prob6())
    print(prob7())
    print(prob8())