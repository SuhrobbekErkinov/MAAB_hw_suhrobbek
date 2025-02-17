def prob1():
    print("---Problem 1---")
    num = float(input("Enter a float number: "))
    print(f"Rounded number to 2 decimal places: {round(num, 2)}")

def prob2():
    print("---Problem 2---")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    num3 = float(input("Enter the 3rd number: "))
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    print(f"The largest number: {largest} \nThe smallest number: {smallest}")

def prob3():
    print("---Problem 3---")
    dist = float(input("Enter a distance in kilometers: "))
    dist_in_m = dist * 1000
    dist_in_cm = dist_in_m * 100
    print(f"{dist} km is {dist_in_m} m\n{dist} km is {dist_in_cm} cm")

def prob4():
    print("---Problem 4---")
    num1 = int(input("Enter the 1st integer number: "))
    num2 = int(input("Enter the 2nd integer number: "))
    largest = max(num1, num2)
    smallest = min(num1, num2)
    int_div = largest // smallest
    int_rem = largest % smallest
    print(f"Integer division: {int_div} \nInteger remainder: {int_rem}")

def prob5():
    print("---Problem 5---")
    temp = float(input("Enter the temperature in celsius: "))
    temp_in_f = temp * 9/5 + 32
    print(f"{temp} C is {temp_in_f} F")

def prob6():
    print("---Problem 6---")
    num = int(input("Enter an integer number: "))
    return num % 10

def prob7():
    print("---Problem 7---")
    num = int(input("Enter an integer: "))
    return num % 2 == 0
def main1():
    print("Number Data Type Questions: ")
    prob1()
    prob2()
    prob3()
    prob4()
    prob5()
    print(prob6())
    print(prob7())
