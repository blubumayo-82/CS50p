def main():
    twttr = input("Input: ")
    output = strip_vowel(twttr)
    print(f"Output: {output}")

def strip_vowel(word):
    twttr = ""
    for char in word:
        if char.lower() in "aeiou":
            continue
        else:
            twttr += char
    return twttr


main()