import sys
import random as rand

# // Get the level the user wants to be play
def get_level() -> int:
    choice: int = 0

    # // While choice is invalid (not 1, 2 or 3)
    while choice not in [1,2,3]:
        try:
            choice = int(input("Level: "))
        except Exception: pass
    return choice

# // Generate a random integer depending
# // on the level choice
def generate_integer(level):
    random_num = 0
    if level == 1:
        random_num = rand.randint(0, 9)
    elif level == 2:
        random_num = rand.randint(10, 99)
    elif level == 3:
        random_num = rand.randint(100, 999)

    return int(random_num)

# // Main function
def main():
    score = 0
    counter = 0
    level = get_level()

    while counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        add = x + y
        answer = int(input(f"{x} + {y} = "))
        tries = 0
        if answer == add:
            counter += 1
            score += 1
        else:
            counter += 1
            while tries < 2:
                if answer == add:
                    tries = 0
                    score += 1
                    break
                elif answer != add:
                    print("EEE")
                    answer = int(input(f"{x} + {y} = "))
                    tries += 1
                if tries == 2:
                    print(f"{x} + {y} = {add}")
    return print(f"Score: {score}")


# // Run the program
if __name__ == "__main__":
    main()