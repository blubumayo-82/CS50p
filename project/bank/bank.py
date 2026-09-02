def main():
    greet = input("Greeting: ")
    money(greet)

def money(greet):
    if greet.strip().lower().startswith('hello'):
        print("$0")
    elif greet.lower().startswith('h'):
        print("$20")
    else:
        print("$100")

main()