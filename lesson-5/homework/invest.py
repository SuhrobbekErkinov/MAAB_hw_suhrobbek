def invest(amount, rate, years):
    """Calculate the investment growth over years."""
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    """Main function to get user input and run the investment calculation."""
    initial_amount = float(input("Enter the initial investment amount: "))
    annual_rate = float(input("Enter the annual percentage rate (as a decimal, e.g., 0.05 for 5%): "))
    num_years = int(input("Enter the number of years: "))

    invest(initial_amount, annual_rate, num_years)

if __name__ == "__main__":
    main()
