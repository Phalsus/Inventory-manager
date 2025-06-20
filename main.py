from utils import utility

def program():
    print("Welcome to Inventory Manager!")

    option = int(input("""[1]-Add New Items
[2]-Update Quantity
[3]-View All Items
[4]-Search Items
[5]-Delete Items
[6]-Exit!
"""))

    match option:
        case 1: utility.addItem()
        case 2: utility.updateQuantity()
        case 3: utility.viewAllItems()
        case 4: utility.search()
        case 5: utility.delete()
        case 6: print("have a good day")
        case _:
            print("invalid option chosen, run the program again")
            program()

program()
