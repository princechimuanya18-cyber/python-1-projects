# this program will track the deposit, withdrawal, expenses and balance 

balance = 0

def deposit():
    # AMOUNT IN DOLLARS
    deposit_amount = float(input("Input amount of deposit: "))              
    return deposit_amount

balance += deposit()

def withdrawal():
    # AMOUNT IN DOLLARS
    withdrawal_amount = float(input("Input amount to withdraw: "))
    if withdrawal_amount > balance:
        print("Insufficient funds.")
    else:
        print("Withdrawal of", withdrawal_amount, "is successful") 
        return withdrawal_amount
    

item_dictionary = {"egg": 2500, "rice": 30000, "beans": 35000, "garri": 15000}
item = ["egg", "rice", "beans", "garri"]

while True:
    item_1 = input("Item to buy(1): ").lower()
    if item_1.lower() in item:
        if item_1 in item_dictionary:
            print("Item in store.")
            if item_1 == item[0]:
                print("The price of", item_1, "is", item_dictionary["egg"])
            elif item_1 == item[1]:
                print("\nThe price of", item_1, "is", item_dictionary["rice"])
            elif item_1 == item[2]:
                print("\nThe price of", item_1, "is", item_dictionary["beans"])
            elif item_1 == item[3]:
                print("\nThe price of", item_1, "is", item_dictionary["garri"])
                break
    item_2 = input("\nItem to buy(2): ").lower()
    
    if item_2.lower() in item:
        if item_2 in item_dictionary:
            print("Item in store.")
            if item_2 == item[0]:
                print("The price of", item_2, "is", item_dictionary["egg"])
            elif item_2 == item[1]:
                print("\nThe price of", item_2, "is", item_dictionary["rice"])
            elif item_2 == item[2]:
                print("\nThe price of", item_2, "is", item_dictionary["beans"])
            elif item_2 == item[3]:
                print("\nThe price of", item_2, "is", item_dictionary["garri"])
                break

            else:
                print("No price for the selected item")

        else: 
             print("Item in store but not in shelf")
    else:
        print("Item not in store")
                
 






