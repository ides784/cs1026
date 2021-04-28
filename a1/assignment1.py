cost = int()
order = ""


def formater(textline):
    textline = textline.lower().strip()
    wordlist = textline.split()
    textline = " ".join(wordlist)
    return textline





looper = 0
while looper == 0:
    try:
        enter_order = input("Enter item (q to terminate): small breakfast, regular breakfast, big "
                            "breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
        if formater(enter_order) == "q":
            break
        elif formater(enter_order) == "egg" or "bacon" or "sausage" or "hash brown" or "toast" or "coffee" or "tea" or "small breakfast" or "regular breakfast" or "big breakfast":
            break
        else:
            print("Error")

    except: ValueError
    continue
    while looper == 0:
        try:
            enter_amount = input("Enter quantity: ")
            if enter_amount.isnumeric():
                break
            else:
                print("Error")
        except: ValueError
        continue

    if formater(enter_order) == "egg":
        cost = cost + (0.99 * int(enter_amount))
    elif formater(enter_order) == "bacon":
        cost = cost + (0.49 * int(enter_amount))
    elif formater(enter_order) == "sausage":
        cost = cost + (1.49 * int(enter_amount))
    elif formater(enter_order) == "hash brown":
        cost = cost + (1.19 * int(enter_amount))
    elif formater(enter_order) == "toast":
        cost = cost + (0.79 * int(enter_amount))
    elif formater(enter_order) == "coffee":
        cost = cost + (1.49 * int(enter_amount))
    elif formater(enter_order) == "tea":
        cost = cost + (1.09 * int(enter_amount))
    elif formater(enter_order) == "small breakfast":
        cost = cost + ((0.99 + 1.19 + (0.79 * 2) + (0.49 * 2) + 1.49) * int(enter_amount))
    elif formater(enter_order) == "regular breakfast":
        cost = cost + (((0.99 * 2) + 1.19 + (0.79 * 2) + (0.49 * 4) + (1.49 * 2)) * int(enter_amount))
    elif formater(enter_order) == "big breakfast":
        cost = cost + (((0.99 * 3) + (1.19 * 2) + (0.79 * 4) + (0.49 * 6) + (1.49 * 3)) * int(enter_amount))
    else:
        print("Error")


tax = cost * 0.13
tax_rounded = round(tax,2)
total = cost + tax_rounded

print("Cost: {}".format(cost))
print("Tax: {}".format(tax_rounded))
print("Total: {:.2f}".format(total))
