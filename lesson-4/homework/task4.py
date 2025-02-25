import random
def guess_the_number():
    while True:
        num = random.randint(1, 100)
        tries = 10

        while tries > 0:
            guess = int(input("Enter an integer between 1 and 100: "))
            if guess > num:
                print("Too high!")
            elif guess < num:
                print("Too low!")
            else:
                print("You guessed it right!")
                return

        print("You lost. Want to play again?\n")
        retry = input().strip().lower()
        if retry not in ['y', 'yes', 'ok', 'lesdothis']:
            break

if __name__ == '__main__':
    guess_the_number()