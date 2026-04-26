## Added a new test file 
def greet_user(branch_name):
    """Prints a formatted greeting for the current branch."""
    # Use f-strings (formatted strings) for clean variable insertion
    message = f"Successfully running code from the '{branch_name}' branch!"
    print(message)

def calculate_simple_interest(principal, rate, time):
    """A small utility function to demonstrate basic math."""
    interest = (principal * rate * time) / 100
    return interest

def main():
    # 1. Basic Output
    print("--- New Test Script Initialized ---")
    greet_user("Other Child Branch")

    # 2. Basic Logic/Math
    p, r, t = 1000, 5, 2
    result = calculate_simple_interest(p, r, t)
    
    print(f"Simple Interest for ${p} at {r}% over {t} years is: ${result}")

# This ensures the code only runs if executed directly
if __name__ == "__main__":
    main()
