def main():
    fuel_f = get_fuel("Fraction: ")
    fuel_p = round(fuel_f * 100)
    if 75 < int(fuel_p) <= 100:
        print("F")
    elif 0 <= int(fuel_p) < 25:
        print("E")
    else:
        print(f"{fuel_p}%")

def get_fuel(prompt):
    while True:
        try:
            fuel_s = input(prompt)
            parts = fuel_s.split('/')
            if len(parts) == 2:
                numerator, denominator = int(parts[0]), int(parts[1])
                if denominator >= numerator:
                    if denominator != 0:
                        fuel_f = numerator / denominator
                        return fuel_f
                    else:
                        print("Zero cannot be the denominator.")
                else:
                    print("Invalid input. Please enter a fraction like '1/2'.")
        except ValueError:
            print("Invalid input. Please enter a fraction like '1/2'.")
        except ZeroDivisionError:
            print("Zero cannot be the denominator.")

if __name__ == "__main__":
    main()
