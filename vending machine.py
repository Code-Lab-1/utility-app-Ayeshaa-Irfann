# define a dictionary of items and their prices
items = {
    "Drinks": {
        "A": {"name": "Coke", "price": 2.50, "stock": 10},
        "B": {"name": "Sprite", "price": 1.50, "stock": 10},
        "C": {"name": "Pepsi", "price": 2.50, "stock": 10},
        "D": {"name": "Fanta", "price": 1.50, "stock": 10},
    },
    "Snacks": {
        "E": {"name": "Snickers", "price": 2.50, "stock": 10},
        "F": {"name": "Twix", "price": 1.50, "stock": 10},
        "G": {"name": "M&M", "price": 2, "stock": 10},
        "H": {"name": "Skittles", "price": 1.50, "stock": 10},
    },
    "Chips": {
        "I": {"name": "Lays", "price": 1.50, "stock": 10},
        "J": {"name": "Cheetos", "price": 3, "stock": 10},
        "K": {"name": "Doritos", "price": 2.50, "stock": 10},
        "L": {"name": "Pringles", "price": 3, "stock": 10},
    },
}
# function to print menu of items
def print_menu(items):
    print("Menu:\n")
    for category, category_items in items.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["name"]} ({item["price"]:.2f} dhs)')
        print()


# function to get valid code from user
def get_code(items):
    while True:
        code = input("Enter code: ")
        # check if code is valid
        for category, category_items in items.items():
            if code in category_items:
                return code
        print("Error: Invalid code. Please try again.")


# function to get valid amount of money from user
def get_money(items, code):
    # search for item in Drinks, Chips and Snacks dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Error: Invalid code "{code}".')
        return

    while True:
        money = float(input("Enter amount of money: "))
        # check if enough money was provided
        if money >= item["price"]:
            return money
        print(
            f'Error: Not enough money. Please insert {item["price"] - money:.2f} dhs more.'
        )


# function to dispense item and calculate change
def dispense_item(items, code, money):
    # search for item in Drinks, Chips and Snacks dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Error: Invalid code "{code}".')
        return

    # check if item is in stock
    if item["stock"] > 0:
        # dispense item and calculate change
        print(f'\nDispensing {item["name"]}...')
        change = money - item["price"]
        item["stock"] -= 1
        print(f"Returning ${change:.2f} change...\n")
    else:
        print(f'\nError: {item["name"]} is out of stock.')


# function to suggest additional purchase based on previous purchase
def suggest_purchase(items, code):
    if code in items["Drinks"]:
        print("You might also like:")
        for code, item in items["Snacks"].items():
            print(f'{code}: {item["name"]} ({item["price"]:.2f}dhs)')
    elif code in items["Snacks"]:
        print("You might also like:")
        for code, item in items["Drinks"].items():
            print(f'{code}: {item["name"]} ({item["price"]:.2f}dhs)')


# print(items["Drinks"]["A"][1])
# main program
while True:
    # print menu of items
    print_menu(items)
    # get valid code from user
    code = get_code(items)
    # get valid amount of money from user
    money = get_money(items, code)
    # dispense item and calculate change
    dispense_item(items, code, money)
    # suggest additional purchase based on previous purchase
    suggest_purchase(items, code)
    # prompt user to continue or exit
    while True:
        response = input("\nWould you like to make another purchase? (y/n) ")
        if response.lower() == "y":
            break
        elif response.lower() == "n":
            print("Thank you for using the vending machine!")
            exit()
        else:
            print("Error: Invalid response. Please try again.")