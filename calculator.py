
import math

# Basic Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponentiate(x, y):
    return x ** y

# Advanced Operations
def sqrt(x):
    if x < 0:
        return "Error: Square root of a negative number"
    return math.sqrt(x)

def log_base(x, base):
    if x <= 0 or base <= 0:
        return "Error: Logarithm of zero or negative number"
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error: Factorial of a negative number"
    return math.factorial(int(x))

def combinations(n, r):
    if n < 0 or r < 0:
        return "Error: Negative values are not allowed"
    if r > n:
        return "Error: r cannot be greater than n"
    return math.comb(int(n), int(r))

# Trigonometric Functions
def trig_sin(x):
    return math.sin(math.radians(x))  # Convert degrees to radians

def trig_cos(x):
    return math.cos(math.radians(x))  # Convert degrees to radians

def trig_tan(x):
    return math.tan(math.radians(x))  # Convert degrees to radians

# Hyperbolic Functions
def hyper_sinh(x):
    return math.sinh(x)

def hyper_cosh(x):
    return math.cosh(x)

def hyper_tanh(x):
    return math.tanh(x)

# Additional Operations
def absolute_value(x):
    return abs(x)

def rounding(x, places):
    return round(x, places)

def truncate(x):
    return int(x)

def gcd(x, y):
    return math.gcd(int(x), int(y))

def lcm(x, y):
    return x * (y // math.gcd(x, y))

def percentage(x, y):
    return (x / y) * 100

def prime_factors(x):
    if x < 2:
        return "No prime factors for values less than 2"
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x //= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            factors.append(i)
            x //= i
    if x > 2:
        factors.append(x)
    return factors

# Calculator Interface
def calculator():
    while True:
        print("\nAdvanced Calculator with Expanded Features")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Logarithm (base-10 or custom base)")
        print("8. Factorial")
        print("9. Combinations (nCr)")
        print("10. Sine (degrees)")
        print("11. Cosine (degrees)")
        print("12. Tangent (degrees)")
        print("13. Hyperbolic Sine")
        print("14. Hyperbolic Cosine")
        print("15. Hyperbolic Tangent")
        print("16. Absolute Value")
        print("17. Rounding")
        print("18. Truncate")
        print("19. Greatest Common Divisor (GCD)")
        print("20. Least Common Multiple (LCM)")
        print("21. Percentage")
        print("22. Prime Factors")
        print("23. Quit")

        choice = input("Choose an operation (1-23): ")

        if choice == '23':
            print("Quitting the calculator. Goodbye!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5', '9']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                elif choice == '5':
                    result = exponentiate(num1, num2)
                elif choice == '9':
                    result = combinations(num1, num2)

            elif choice in ['6', '7', '8', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']:
                num1 = float(input("Enter a number: "))
                if choice == '6':
                    result = sqrt(num1)
                elif choice == '7':
                    base = float(input("Enter the base for the logarithm (default is 10): "))
                    result = log_base(num1, base)
                elif choice == '8':
                    result = factorial(num1)
                elif choice == '10':
                    result = trig_sin(num1)
                elif choice == '11':
                    result = trig_cos(num1)
                elif choice == '12':
                    result = trig_tan(num1)
                elif choice == '13':
                    result = hyper_sinh(num1)
                elif choice == '14':
                    result = hyper_cosh(num1)
                elif choice == '15':
                    result = hyper_tanh(num1)
                elif choice == '16':
                    result = absolute_value(num1)
                elif choice == '17':
                    places = int(input("Enter the number of decimal places to round to: "))
                    result = rounding(num1, places)
                elif choice == '18':
                    result = truncate(num1)
                elif choice == '19':
                    num2 = float(input("Enter the second number: "))
                    result = gcd(num1, num2)
                elif choice == '20':
                    result = lcm(num1, num2)
                elif choice == '21':
                    num2 = float(input("Enter the whole amount to get the percentage of: "))
                    result = percentage(num1, num2)
                elif choice == '22':
                    result = prime_factors(num1)

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

# Run the calculator
calculator()
