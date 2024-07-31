import emoji

def main():
    string = get_str("Input: ")
    print(emoji.emojize(string))

def get_str(prompt):
    string = input(prompt)
    return string

main()