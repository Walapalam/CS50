camel_case = input("CamelCase: ")
words = []

start = 0  # Start index of the current word

for index, char in enumerate(camel_case):
    if char.isupper():
        if start < index:
            words.append(camel_case[start:index].lower())
        start = index

# Add the last word
if start < len(camel_case):
    words.append(camel_case[start:].lower())

snake_case = '_'.join(words)
print("SnakeCase:", snake_case)
