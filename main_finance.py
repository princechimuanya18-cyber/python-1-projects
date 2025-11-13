import finance


print(
'''
+=============================+
|  WELCOME TO CHIJULY FINANCE
|         TRACKER
+=============================+
''')

customer_balance = finance.balance

Menu = {
    "1": finance.deposit(), 
    "2": finance.withdrawal(),
    "3": finance.customer_balance
}



# Customer input
choice = input("Choose Menu(1-3): ")
if choice == "1":
    print("Amount deposited is", finance.deposit())
elif choice == "2":
    print("Your withdrawal of", finance.withdrawal,(), "was successful")
elif choice == "3":
    print("Your current balance is", customer_balance)
else:
    print("Invalid option")

shop_list = str(input("Would you love to get our item list(yes/no): "))
if shop_list == "yes":
    print(
    f'''
    +=================================+
                ITEM LIST
    +=================================+
    | {finance.item_1: item_dictionary["egg"] or item_dictionary["rice"] \
       or item_dictionary["beans"] or item_dictionary["garri"]}
    | {finance.item_2: item_dictionary["egg"] or item_dictionary["rice"] \
       or item_dictionary["beans"] or item_dictionary["garri"]}
    +=================================+
    ''')
print()
print(
'''
==========================
    THANK YOU
==========================
''')