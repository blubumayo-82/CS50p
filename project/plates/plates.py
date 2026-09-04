def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            if char == "0":
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


main()