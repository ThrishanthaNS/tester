# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main function to run the program
if __name__ == "__main__":
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the function to add the numbers
    result = add_numbers(num1, num2)
    
    # Output the result
    print(f"The sum of {num1} and {num2} is {result}.")
