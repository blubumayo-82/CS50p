def main():
    operation = input("Enter a whole mathematical expression (x + y): ")
    x, op1, y = operation.split()
    x = float(x)
    y = float(y)

    answer = calculate(x, op1, y)
    if answer is not None:
        print(f"The answer is: {answer:.2f}")

def calculate(x, op1, y):
    match op1:
        case "+":
            result1 = x + y
        case "-":
            result1 = x - y
        case "*":
            result1 = x * y
        case "/":
            if y == 0:
                print("Cannot divide by zero")
                return None
            result1 = x / y
        case _:
            print(f"Operator '{op1}' invalid")
            return None
    return float(result1)


main()