import math

def main():
    # Get valid x value from user
    while True:
        try:
            x = float(input("Enter a value for x: "))
            if 0 < x <= 2:
                break
            else:
                print("Out of range! Try again: ", end="")
        except ValueError:
            print("Invalid input! Please enter a number. Try again: ", end="")
    
    # Get tolerance from user
    while True:
        try:
            tolerance = float(input("Enter the tolerance: "))
            if tolerance > 0:
                break
            else:
                print("Tolerance must be positive. Try again: ", end="")
        except ValueError:
            print("Invalid input! Please enter a number. Try again: ", end="")
    
    # Calculate ln(x) using Taylor series expansion
    # ln(x) = (x-1) - (x-1)^2/2 + (x-1)^3/3 - (x-1)^4/4 + ...
    
    approximation = 0
    n = 1
    x_minus_1 = x - 1
    
    while True:
        # Calculate the nth term: (-1)^(n+1) * (x-1)^n / n
        term = ((-1) ** (n + 1)) * (x_minus_1 ** n) / n
        
        # Check if the absolute value of the term is less than tolerance
        if abs(term) < tolerance:
            break
            
        # Add the term to our approximation
        approximation += term
        n += 1
    
    # Calculate exact value using math.log
    exact_value = math.log(x)
    
    # Calculate difference
    difference = abs(approximation - exact_value)
    
    # Print results
    print(f"ln({x}) is approximately {approximation}")
    print(f"ln({x}) is exactly {exact_value}")
    print(f"The difference is {difference}")

if __name__ == "__main__":
    main()