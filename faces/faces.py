string = input("Enter emoji: ")

string = string.split()
converted_strings = []

for emoji in string:
    if emoji == ":)":
        converted_strings.append("🙂")
    elif emoji == ":(":
        converted_strings.append("🙁")
    else:
        converted_strings.append(emoji)

for i in converted_strings:
    print(i, end = " ")
