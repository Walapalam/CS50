def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha = 0
    digit = 0
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s.isalpha():
                return True
            for index, char in enumerate(s):
                if char.isdigit():
                    alpha = s[:index]
                    digit = s[index:]
                    break
        else:
            return False
    else:
        return False
    if digit[0] == 0 or digit[0] == "0":
        return False


    if str(alpha).isalpha() and digit.isdigit():
        return True

if __name__ == "__main__":
    main()
