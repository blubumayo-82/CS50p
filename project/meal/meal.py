def main():
    time = input("What time is it? ").strip()
    time_final = convert(time)

    if 7.0 <= time_final <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_final <= 13.0:
        print("lunch time")
    elif 18.0 <= time_final <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()