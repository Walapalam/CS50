def main():
    time = input("What time is it? ")
    time = convert(time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)

    total_hours = hour +  minutes/60
    return total_hours


if __name__ == "__main__":
    main()