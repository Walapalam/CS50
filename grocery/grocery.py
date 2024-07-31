def main():
    list = {}
    while True:
        try:
            item = get_item()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            for items, index in sorted(list.items()):
                print(index, items.upper())
            break


def get_item():
    item = input()
    item = item.lower()
    return item

main()