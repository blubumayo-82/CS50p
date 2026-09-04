def main():
    mass = int(input("m: "))
    print(convert(mass))

def convert(kg):
    mass = kg * (300000000)**2
    return mass

main()    