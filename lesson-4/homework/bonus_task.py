import random
def rock_scissors_paper():
    choices = ['rock', 'paper', 'scissors']
    choices1 = ['r', 'p', 's']
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter rock(r), paper(p) or scissors(s): ").strip().lower()
        computer_choice = random.choice(choices)

        if player_choice not in choices and player_choice not in choices1:
            print("Invalid input, try again\n")
            continue

        print(f'Computer chose {computer_choice}')
        if player_choice == computer_choice[0]:
            print("It is a tie!")
        elif ((player_choice == 'rock' or player_choice == 'r') and computer_choice == 'scissors') or \
                ((player_choice == 'scissors' or player_choice == 's') and computer_choice == 'paper') or \
                ((player_choice == 'paper' or player_choice == 'p') and computer_choice == 'rock'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")

    print("You won!" if player_score == 5 else "Computer won!")

if __name__ == '__main__':
    rock_scissors_paper()


