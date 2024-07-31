import inflect

def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            names = get_name("Name: ")
            name_list.append(names)
        except EOFError:
            break
    if len(name_list) != 0:
        names = p.join(name_list)
        print(f"Adieu, adieu, to {names}")

def get_name(prompt):
    name = input(prompt)
    return name

main()

