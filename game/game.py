import random

def main():
    n = get_int("Level: ")
    number = random.randint(1, n)
    guess = get_guess("Guess: ")

    if number == guess:
        print("Just right!")
    else:
        while True:
            if number == guess:
                print("Just right!")
                break
            if number < guess:
                print("Too large!")
                guess = get_guess("Guess: ")
            elif number > guess:
                print("Too small!")
                guess = get_guess("Guess: ")

def get_int(prompt):
    try:
        num = int(input(prompt))
        if num <= 0:
            raise Exception
        return num
    except (ValueError, Exception):
        return get_int(prompt)

def get_guess(prompt):
    try:
        num = int(input(prompt))
        if num <= 0:
            raise Exception
        return num
    except (ValueError, Exception):
        return get_guess(prompt)

if __name__ == "__main__":
    main()
