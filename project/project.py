import datetime
import random

# Declaring necessary variables into Global variables to be accessed throughout the program
global playerName, lifeScore, attempt, result, random_numbers
playerName = str
lifeScore = 0
attempt = 0
random_numbers = list
result = []

def main():
    """ The Main Program Function which calls different functions for the DON Game to work
    """

    # Call get_name function for the player's name
    playerName = get_name("Player Name: ")

    # Adding into the results to be written into the word file
    result.append(f"Player Name: {playerName}\n")

    # Generating the life score through random module
    lifeScore = random.randint(1, 50)

    # Printing the game ui as well as appending to the results for text file integration
    for attempt in range(1, 22):
        if attempt == 21:
            print(gameStatus(playerName, lifeScore, attempt))
            result.append(gameStatus(playerName, lifeScore, attempt))
            saveToFile(result)
            break

        print(f"Attempt {attempt}")
        lifeScoreString = f"{playerName}'s Life Score is: {lifeScore}"
        print(lifeScoreString)

        result.append(f"""
Attempt {attempt}
{playerName}'s Life Score is: {lifeScore}
{lifeScoreString}""")

        # Generate random number array and printing it
        random_numbers = generateRandomNumbers(attempt)
        for randomNumber in random_numbers:
            print(randomNumber, end=" ")
            result.append((str(randomNumber) + " "))

        # Selection of Digit from random number array
        selectedNumber = selectionOfDigit(random_numbers)
        result.append(f"\nSelect a number to fight: {selectedNumber}")

        if selectedNumber <= lifeScore:
            lifeScore += selectedNumber

            print(f"{playerName} killed {selectedNumber}\n")
            result.append(f"{playerName} killed {selectedNumber}\n\n")

            continue
        else:
            print(f"{selectedNumber} killed {playerName}")
            print(gameStatus(playerName, lifeScore, attempt))

            result.append(f"""
{selectedNumber} killed {playerName}
{gameStatus(playerName, lifeScore, attempt)}\n""")

            # Call the function to save to the file by providing result list as the argument
            saveToFile(result)
            break


def saveToFile(ResultList):
    """ By taking the result list as the argument, the function creates a file with current, date and time using
    datetime module now function, then appends all the results of the game.
    """
    year, month, date = str(datetime.datetime.now())[:10].split("-")
    hour, minutes, seconds = str(datetime.datetime.now())[11:19].split(":")

    fileName = f"{year}_{month}_{date}_{hour}_{minutes}_{seconds}_{random.randint(0, 9999)}"
    with open(f"{fileName}.txt", "a+") as textFile:
        for item in ResultList:
            textFile.write(str(item))


def selectionOfDigit(listOfNumbers):
    """ By taking a list of numbers as the argument, functions handles errors such as ValueError and availability of
    selected number in list. Also appends into the results when error is raised and exits after calling the file saving
    function
    """
    selection = input("\nSelect a number to fight: ")
    try:
        if int(selection) in listOfNumbers:
            return int(selection)
        else:
            print("No Such Enemy")
            print(gameStatus(playerName, lifeScore, attempt))

            result.append(f"""
Select a number to fight:{selection}
No Such Enemy
{gameStatus(playerName, lifeScore, attempt)}\n""")

            saveToFile(result)
            exit()
    except ValueError:
        print("No Such Enemy")
        print(gameStatus(playerName, lifeScore, attempt))

        result.append(f"""
Select a number to fight:{selection}\n
No Such Enemy
gameStatus(playerName, lifeScore, attempt)\n""")

        saveToFile(result)
        exit()


def gameStatus(PlayerName, LifeScore, Attempt):
    """ By taking name, score and attempt as the arguments, the function returns a formatted string with game status.
    """
    if attempt < 21:
        return (f"""
*** Game Status ***
Player Name: {PlayerName}
Total Attempts: {Attempt}
Final Score: {LifeScore}
{PlayerName} was defeated !!!

Thanks for Playing!!
    """)
    else:
        return (f"""
*** Game Status ***
Player Name: {playerName}
Total Attempts: {attempt}
Final Score: {lifeScore - 1}
{playerName} saved the Kingdom!!!

Thanks for Playing!!
    """)


def generateRandomNumbers(Attempt):
    """ By taking attempt as the argument, creates five random numbers according to the attempts and returns a list of
    random numbers. Also manages the exceeding of attempt count.
    """
    if Attempt > 20:
        return print("Attempts Finished")

    if Attempt <= 5:
        return random.sample(range(15, 101), k=5)

    elif 5 < Attempt < 11:
        return random.sample(range(250, 2001), k=5)

    elif 11 <= Attempt < 16:
        return random.sample(range(3000, 10001), k=5)

    elif 16 <= Attempt < 21:
        return random.sample(range(20000, 100001), k=5)


def get_name(prompt):
    """ By taking the prompt as the argument, returns the name if the name is valid. Validity is checked through the
    content of the name to be alphanumerical values.
    """
    while True:
        try:
            name = input(prompt)
            if name.isnumeric():
                raise Exception
            else:
                return name
        except:
            print("Invalid Entry")


# For support in "import as" call
if __name__ == "__main__":
    main()

