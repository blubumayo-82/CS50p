def main():
    sentence = input("")
    print(convert(sentence))

def convert(to_emoji):
    to_emoji = to_emoji.replace(":)", "🙂").replace(":(", "🙁")
    return to_emoji

main()