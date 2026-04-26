def fibonacci(n):
    """A simple recursive function to find the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("--- Welcome to the Fibonacci Explorer ---")
    
    try:
        count = int(input("How many numbers of the sequence would you like to see? "))
        
        if count <= 0:
            print("Please enter a positive integer!")
        else:
            print(f"\nGenerating the first {count} numbers:")
            sequence = [str(fibonacci(i)) for i in range(count)]
            print(" -> ".join(sequence))
            print("\nSequence complete. Math is beautiful, isn't it?")
            
    except ValueError:
        print("Oops! That wasn't a number. Try again next time!")

if __name__ == "__main__":
    main()
