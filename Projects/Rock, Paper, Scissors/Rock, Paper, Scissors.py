import random

def get_user_choice():
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Your choice (1/2/3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice! Please choose 1, 2, or 3.")
        choice = input("Your choice (1/2/3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    outcomes = {
        (1, 3): "You win! Rock crushes Scissors.",
        (2, 1): "You win! Paper covers Rock.",
        (3, 2): "You win! Scissors cut Paper.",
        (3, 1): "You lose! Rock crushes Scissors.",
        (1, 2): "You lose! Paper covers Rock.",
        (2, 3): "You lose! Scissors cut Paper.",
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    return outcomes.get((user_choice, computer_choice), "Something went wrong.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    choices_map = {1: "Rock", 2: "Paper", 3: "Scissors"}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {choices_map[user_choice]}")
        print(f"Computer chose: {choices_map[computer_choice]}")
        
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
