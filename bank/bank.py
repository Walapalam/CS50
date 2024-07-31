def main():
    greeting = input("Greeting: ").lower()

    greeting = greeting.split()
    print(value(greeting))

def value(list):
    hello = "hello"
    for greet in list:
        if greet == hello or greet == hello + ",":
            return("$0")
        elif greet.startswith("h"):
            return("$20")
        else:
            return("$100")
        break

if __name__ == "__main__":
    main()