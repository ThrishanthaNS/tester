def fibonacci(n):
    # Starting values for the Fibonacci series
    a, b = 0, 1
    
    # Generate and print the Fibonacci series up to n terms
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update values of a and b for the next term

# Main function to run the program
if __name__ == "__main__":
    # Ask the user for the number of terms in the Fibonacci series
    n = int(input("Enter the number of terms in Fibonacci series: "))
    
    # Generate the Fibonacci series
    fibonacci(n)
