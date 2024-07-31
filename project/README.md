    # YOUR PROJECT TITLE
    #### Video Demo:  https://www.youtube.com/watch?v=xeoxz03f2sk
    #### Description:
    “DON (Destroyer of Numbers)” is known to the Kingdom as a hero who saved them from evil numbers. DON kills numbers by selecting values which are lower than his “Life Score”. This allows him to climb up the levels. He is given 20 chances per session. If he survives all the 20 chances he wins. If not, he dies!
    #### Code Description:
    The program works with a main function which calls the necessary functions for the game to run. The code uses modules such as Datetime and Random and calls upon the necessary functions. The game UI is implemented in console, the variables such as life score, random number list are generated through the random module and date, time are generated through datetime module. The whole UI is appended to the text file and output to the folder with the code.

    The functionality of the code works with the prompting for the users name, where numbers arent allowed. In a case where numbers are entered, the code re-prompts the user until a proper name is entered. Then the user is assigned a life score from 1 to 50, and presented with 5 random selection numbers from range 15 to 100. (The selection ranges updates according to the attempt number). If the user selects a valid number from the list that is lower than the lifescore, the lifescore is updated with the selection numbers, else the user is defeated and the program ends with displaying the end game status as losing. The repeating is done through a for loop, where the range is set to be from 1 to 22, in the case where the attempt reaches 21, the end game status is displayed as the user winning the game. Finally when end game status is displayed, the output is appended onto a text file with date and time as the text file name.

    #### Test Cases:
    The Test Cases are listed below and the validations from the code will be mentioned in the video with necessary descriptions,
    1. Valid Name Input : Code proceeds, and shows “Attempt 1”, Life Score, 5 random numbers from range 1-100, and a prompt for selection
    2. Invalid Name Input : Re-prompts user for suitable name until valid name is entered
    3. Valid Selection Input(Winning) : 37 is entered, where life score is 78. Since 37 is present and lesser than life score, life score is updated to 78 and attempt 2 prompts are displayed
    4. Valid Selection Input(Loosing) : 96 is entered where life score is 46. Since 96 is greater than life score, 46, player is defeated, and end game status is shown
    5. Invalid Selection Input(Integer not in selection list) : 23 is entered, where 23 isnt an option in the list. Since 23 isn’t in the random number list, the programs outputs “No Such Enemy” and shows end game status
    6. Invalid Selection Input (Non-Integer Input) : Since strings aren’t in the random number list, the programs outputs “No Such Enemy” and shows end game status
    7. Valid Selection Ranges According to Attempt : Selection Ranges update according to the attempt count, and shows winning end game status when attempt reaches 21
    8. Game Completion Message : As player has finished all 20 rounds, the game ends with winning end game status
    9. Valid Text File Integration : Proper date and time are set as file name and text file contains all attempts information

     
