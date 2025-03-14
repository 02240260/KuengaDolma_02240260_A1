import random  # Importing the random module to generate random numbers for games

# Function for Guess Number Game
def guess_number_game():
    print("\nWelcome to the Guess Number Game!")  # Welcome message
    
    # The computer will randomly choose a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Loop until the user guesses the correct number
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))  # Asking the user to guess
            if user_guess < number_to_guess:  # If the guess is too low
                print("Too low! Try again.")
            elif user_guess > number_to_guess:  # If the guess is too high
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the right number.")
                break  # End the loop when the user guesses correctly
        except ValueError:  # If the user does not enter a valid number
            print("Please enter a valid number.")
    
# Function for Rock Paper Scissors Game
def rock_paper_scissors_game():
    choices = ['rock', 'paper', 'scissors']  # The three options for the game
    
    print("\nWelcome to Rock Paper Scissors!")  # Welcome message
    print("Choices are: rock, paper, or scissors.")  # Inform the user of choices
    
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()  # User input, converting to lowercase
    
    # Check if the user entered a valid choice
    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")  # If invalid input
        return  # Exit the function if the input is invalid
    
    # The computer randomly picks one of the choices
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")  # Show computer's choice
    
    # Determine the winner using game rules
    if user_choice == computer_choice:
        print("It's a tie!")  # If both choices are the same
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win this round!")  # If the user wins
    else:
        print("You lose this round!")  # If the user loses

# Main program to display the menu and select a game
def main():
    while True:  # Start a loop so the program keeps running until the user chooses to exit
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")  # Option 1
        print("2. Rock Paper Scissors game")  # Option 2
        print("3. Exit program")  # Option 3
        
        # Ask for user input to select a function
        choice = input("Enter your choice: ")
        
        if choice == '1':  # If the user selects the Guess Number game
            guess_number_game()
        elif choice == '2':  # If the user selects the Rock Paper Scissors game
            rock_paper_scissors_game()
        elif choice == '3':  # If the user selects Exit
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please select a number between 1 and 3.")  # If the user enters an invalid choice

# Call the main function to start the program
main()
