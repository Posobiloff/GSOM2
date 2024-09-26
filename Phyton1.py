# 1. INT, FLOAT. The simple code that computes the discriminant using only int numbers.
print("Now we're going to calculate discriminant for a*x² + b*x + c = 0")

def get_numeric_input(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

a = get_numeric_input("Input variable a: ")
b = get_numeric_input("Input variable b: ")
c = get_numeric_input("Input variable c: ")

D = b * b - 4 * a * c

if D < 0:
    print("No roots, D < 0")
elif D == 0:
    x = -b / (2 * a)
    print(f"One root: {x}")
else:
    x1 = (-b - D**0.5) / (2 * a)
    x2 = (-b + D**0.5) / (2 * a)
    print(f"Two roots: {x1} and {x2}")
