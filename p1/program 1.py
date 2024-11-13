def is_palindrome(num):
    original_number = num  # Store the original number
    reversed_number = 0

    # Reverse the number
    while num != 0:
        last_digit = num % 10  # Get the last digit
        reversed_number = reversed_number * 10 + last_digit  # Build the reversed number
        num //= 10  # Remove the last digit from num
    
    # Check if the original number is equal to the reversed number
    return original_number == reversed_number

# Main function to run the program
if __name__ == "__main__":
    # Ask the user for input
    num = int(input("Enter a number: "))

    # Call the function to check if the number is a palindrome
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
