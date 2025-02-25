def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

def main():
    """Main function to handle user input and conversion."""
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    print(f"{fahrenheit} degrees F = {convert_far_to_cel(fahrenheit)} degrees C")

    celsius = float(input("\nEnter a temperature in degrees C: "))
    print(f"{celsius} degrees C = {convert_cel_to_far(celsius)} degrees F")

if __name__ == "__main__":
    main()
