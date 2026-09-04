def main():
    text = input("Input: ")
    shortened = shorten(text)
    print(f"Output: {shortened}")


def shorten(word):
    strip = ""
    for char in word:
        if char.lower() not in "aeiou":
            strip += char
    return strip


main()