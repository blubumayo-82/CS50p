def main():
    camel = input("camelCase: ")
    snake = convert_snake(camel)
    print("snake_case:", snake)

def convert_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


main()