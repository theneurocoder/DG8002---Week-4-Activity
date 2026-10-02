# DG8002 - F26 - Activity 4
# Author Name: Abdullah Alhomoud
# Date: 2026-10-02

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

# TODO 1: Print out the entire menu and the price of each item
for item in menu:
    print(item + ": " + format(menu[item], ".2f"))

ordering = True

# TODO 2: Start a loop, asking the customer which item they would like to order
while ordering:

    # TODO 3: If the customer types a word check whether the requested item exists
    typedItem = input("What would you like to order? Type an item and 'Done' when you are done: ").capitalize()

    # TODO 4: Add valid items to the customer's order and let the loop continue
    if typedItem in menu:
        order.append(typedItem)

    # TODO 5: if the customer types "Done", end the loop and move to end of order
    elif typedItem == "Done":
        ordering = False


# TODO 6: Print out an itemized receipt for the user showing item and cost

totalCost = 0

print("Order:")

for orderItem in order:
    for menuItem in menu:
        if orderItem == menuItem:
            print(menuItem + ": " + format(menu[menuItem], ".2f") )
            totalCost = totalCost + menu[menuItem]
# TODO 7: Print out the subtotal of the entire order
print("Total cost: " + format(totalCost, ".2f"))


# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
