from pyfiglet import Figlet
import sys

# // If invalid font argument
if sys.argv[1] not in ["-f", "-font"]:
    sys.exit("Invalid usage")

# // Get the user input
inp: str = input("Input: ")

# // Initialize figlet modules
figlet = Figlet()
figlet.getFonts()

# // Set the figlet font
figlet.setFont(font = sys.argv[2])

# // Print the rendered text
print(figlet.renderText(inp))