def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    clean_d = d.replace("$", "")
    final_d = float(clean_d)
    return final_d


def percent_to_float(p):
    clean_p = p.replace("%", "")
    final_p = float(clean_p) * 0.01
    return final_p


main()
