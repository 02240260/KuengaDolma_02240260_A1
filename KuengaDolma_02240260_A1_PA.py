import os  # Importing os module to check if file exists

# Function to check if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Checking divisibility from 2 to sqrt(n)
        if n % i == 0:
            return False
    return True

# Function to calculate the sum of prime numbers in a given range
def prime_sum():
    """Calculate the sum of prime numbers in a given range."""
    try:
        start = int(input("Enter start number: "))  # Getting start range from user
        end = int(input("Enter end number: "))  # Getting end range from user
        primes = [num for num in range(start, end + 1) if is_prime(num)]  # List comprehension for prime numbers
        print(f"Sum of primes: {sum(primes)}")  # Printing sum of primes
    except ValueError:
        print("Invalid input! Please enter numbers only.")  # Handling invalid inputs

# Function to convert between meters and feet
def length_converter():
    """Convert between meters and feet."""
    try:
        value = float(input("Enter length: "))  # Getting numerical value
        unit = input("Enter 'M' for meters to feet, 'F' for feet to meters: ").strip().upper()  # Getting conversion unit
        if unit == 'M':
            print(f"{value} meters = {round(value * 3.28084, 2)} feet")  # Converting meters to feet
        elif unit == 'F':
            print(f"{value} feet = {round(value / 3.28084, 2)} meters")  # Converting feet to meters
        else:
            print("Invalid unit! Please enter 'M' or 'F'.")  # Handling invalid input
    except ValueError:
        print("Invalid input! Please enter a number.")  # Handling invalid input

# Function to count consonants in a given string
def consonant_counter():
    """Count consonants in a string."""
    text = input("Enter a string: ")  # Getting user input
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # Defining consonant letters
    count = sum(1 for char in text if char in consonants)  # Counting consonants using list comprehension
    print(f"Number of consonants: {count}")  # Printing result

# Function to find the smallest and largest number from user input
def min_max_finder():
    """Find the smallest and largest number from user input."""
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))  # Getting list of numbers
        if nums:
            print(f"Smallest: {min(nums)}, Largest: {max(nums)}")  # Finding min and max
        else:
            print("No numbers entered.")  # Handling empty input
    except ValueError:
        print("Invalid input! Please enter numbers only.")  # Handling invalid input

# Function to check if a string is a palindrome
def palindrome_checker():
    """Check if a string is a palindrome."""
    text = input("Enter a string: ").replace(" ", "").lower()  # Removing spaces and converting to lowercase
    print("True" if text == text[::-1] else "False")  # Checking if reversed text is the same

# Function to count specific words in a text file
def word_counter():
    """Count occurrences of specific words in a text file."""
    words_to_count = ["the", "was", "and"]  # Words to count in the file
    try:
        if not os.path.exists("sample.txt"):  # Checking if file exists
            print("File not found! Make sure 'sample.txt' exists.")
            return
        with open("sample.txt", "r") as file:  # Opening file for reading
            text = file.read().lower().split()  # Reading file content, converting to lowercase, and splitting into words
            counts = {word: text.count(word) for word in words_to_count}  # Counting whole-word occurrences
            for word, count in counts.items():
                print(f"{word}: {count}")  # Printing word count
    except Exception as e:
        print(f"Error reading file: {e}")  # Handling file errors

# Main menu function
def main_menu():
    """Main menu for selecting functions."""
    while True:
        print("\nSelect a function (1-6):")  # Displaying menu options
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")

        choice = input("Enter your choice: ")  # Getting user choice

        if choice == "1":
            prime_sum()
        elif choice == "2":
            length_converter()
        elif choice == "3":
            consonant_counter()
        elif choice == "4":
            min_max_finder()
        elif choice == "5":
            palindrome_checker()
        elif choice == "6":
            word_counter()
        elif choice == "0":
            print("Goodbye!")  # Exiting program
            break
        else:
            print("Invalid choice! Please enter a number between 0-6.")  # Handling invalid input
        
        retry = input("Would you like to try another function? (y/n): ").strip().lower()
        if retry != 'y':
            print("Goodbye!")
            break

# Running the main menu
if __name__ == "__main__":
    main_menu()

