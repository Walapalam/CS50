string = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().replace(" ", "")

match string:
    case "42" | "fortytwo" | "forty-two":
        print("Yes")
    case _:
        print("No")