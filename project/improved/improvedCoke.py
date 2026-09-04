def main():
    owe = 50

    while owe > 0:
        print(f"Amount Due: {owe}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            owe -= coin

    print(f"Change Owed: {abs(owe)}")


main()