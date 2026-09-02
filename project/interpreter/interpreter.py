def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    interpret(x, y, z)

def interpret(x, y, z):
    x = float(x)
    z = float(z)

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        if z != 0:
            print(x / z)
    
main()