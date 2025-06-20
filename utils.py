import json

with open("data.json", "r") as file:
    data = json.load(file)

class utility:
    def addItem():
        name = input("Enter item name: ").lower()
        for i in data["inventory"]:
            if i["name"] == name:
                print("item already exist")
                return
        description = input("Enter item description").lower()
        quantity = input("Enter the quantity of the item(s)")
        newItem = {
            "name":name,
            "description":description,
            "quantity":quantity,
        }
        data["inventory"].append(newItem)
        with open("data.json", "w") as file:
            json.dump(data, file)
        return

    def updateQuantity():
        name = input("what item do you want to change? : ").lower()
        valid = False
        for i in data["inventory"]:
            if i["name"] == name :
                valid =True
                quantity = input("what is the new quantity? :")
                i["quantity"] = quantity
        if not valid:print("that item does not exist")
        with open("data.json", "w") as file:
            json.dump(data, file)
        return

    def viewAllItems():
        for i in data["inventory"]:
            print(i["name"],i["description"],i["quantity"])
        return

    def search():
        name = input("what item are you looking for? : ").lower()
        valid = False
        for i in data["inventory"]:
            valid = True
            if i["name"] == name :
                print(i["name"],i["description"],i["quantity"])
        if not valid:print("that item does not exist")
        return

    def delete():
        name = input("what item do you want to delete? ").lower()
        valid = False
        for i in data["inventory"]:
            valid = True
            if i["name"] == name :
                print(data["inventory"])
                data["inventory"].remove(i)
        if not valid:print("that item does not exist")
        with open("data.json", "w") as file:
            json.dump(data, file)
        return