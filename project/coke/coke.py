def main():
    print("Amount Due: 50")
    amount_due()
    
def amount_due():
    owe = 50
    while owe > 0:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            owe -= coin
        if owe < 0:
            continue
        print("Amount Due:", owe)
    change = owe - (owe * 2)
    print("Change Owed:", change)


main()