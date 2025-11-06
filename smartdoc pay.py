# program for the "smartdoc" project
# the smartdoc which is a program that allows users to makes efficient payment
# to any of the list of diagnosis and employs the use of smart Trust wallet deposits of 10%
# for future savings.
# for every of the patient's transaction made.


#Welcome interface
print(
'''
\t\t====================================
\t\t\tHI # WELCOME TO SMARTDOC #
\t\t==================================== 
''')

def time_count():                               #used to time speed inputs
    print("\n⏳ Verifying password...")
    time.sleep(1)
    print("\n📡 Beep...")
    time.sleep(1)
    print("📡 Beep...") 
    time.sleep(1)

def normal_count():                             #Ffor normal time beep
    print("\nWait for a moment....")
    time.sleep(1)

import time 

patient_name = input("User name: ")   #input of patients name


normal_count()
#Create password or log_in interface
print("\nWELCOME", patient_name.upper(), "TO SMARTDOC PAY #")
create_password = str(input("\nAlready have a password(yes/no): "))



attempt = 0
if create_password.lower() == "yes":
    pin_1 = input("Input your pin:  ")
    while True:
        log_in_password = input("Input your password: ")   #must end wih SD
        pin = input("Input four digit pin(****): ")
        if log_in_password.endswith("SD"):
            if pin == pin_1:
                time_count()
                print("Access granted #")
                break
        else:
            attempt += 1
            final_attempt = 3
            current_attempt = final_attempt - attempt
            time_count()
            print("\n❌ Invalid password. You have", current_attempt, "more attempts.")
            if attempt == 3:
                print("🚫 Too many attempts. System locked 🔐", end=" ")  # system goes temporarily locked
                print("⏰ Try again in 10 minutes.")
                exit()
        # password creation
else:   
    new_password = input("\nCreate new password(must end with SD): ")
    pin_2 = input("\nCreate four digit pin(****): ")
    if new_password.endswith("SD"):
        normal_count()   
        print()
        while True:
            log_in = input("Enter password: ")  #the password is created successfully with SD
            pin_2a = input("Enter four digit pin(****): ")
            if log_in == new_password:
                if pin_2a == pin_2:                     #four digit pin that matches pin_2
                    time_count()
                    print("Access granted #")
                    break
            else:
                attempt += 1
                final_attempt = 3
                current_attempt = final_attempt - attempt
                time_count()
                print("\n❌ Invalid password. You have", current_attempt, "more attempts.")
                if attempt == 3:
                    print("🚫 Too many attempts. System locked 🔐", end=" ")  # system goes temporarily locked
                    print("⏰ Try again in 10 minutes.")
                    exit()

            
#patients finance data



#patient examination
#{examination: price in dollars}

# Example data for each ward
Radiology_examinations = {             
    "MRI": 2000 , 
    "ULTRASOUND": 600, 
    "X-RAY": 700, 
    "FLUOROSCOPY": 800, 
    "SPECIALS": 450
}                              

Histopathology_examinations = {
    "AUTOPSY": 1300, 
    "TISSUE PROCESSING": 450,                
    "MORBID": 5000, 
}
Hematology_examinations = {
    "M.P": 50,        #malaria parasite
    "WIDAL": 60,      # Typhoid test
    "PCV": 80,        # Packed Cell Volume for RBC and WBC
    "WBC COUNT": 50,  #test for White Blood cell
    "HEMOGLOBIN": 50  #tetst for Hemoglobin level in RBC
}

Fertility_examinations = {
    "IVF": 1e4,                  #In-vitro fertilization
    "SEMEN ANALYSIS": 2000,
    "HORMONE SCREENING": 2500,
    "TESTICULAR BIOPSY": 4500
}

# Combine all units into one dictionary
hospital_units = {
    "RADIOLOGY": Radiology_examinations,
    "HISTOPATHOLOGY": Histopathology_examinations,
    "HEMATOLOGY": Hematology_examinations,
    "FERTILITY": Fertility_examinations
}
#options for users monetary activities
transaction_options = {
    1: "Check balance",
    2: "Deposit",
    3: "Check Smartaccount balance",
    4: "Make payment",
    5: "exit()"
}

# create a system where the patient will be prompted  to pay for the hosputal bill
#if its balance isn't enough, then the user will be prompted to deposit

patient_balance = 0  #assuming the patient is on a zero account balance
smart_account_balance = 0  #current savings system of the patient

# Ask the patient to choose a ward
unit_choice = input("unit name to make pament: ").upper()
normal_count()
if unit_choice in hospital_units:
    print("\nWelcome to the " + unit_choice.title() + " Ward 🏥")                   # Welcome line of the progeram chosen by the user 
    print("You can now proceed to making payments 💳")                      # line for making payments

    ward_data = hospital_units[unit_choice]
    print (             # the table used to guide patients on what examination to choose in the unit
    f'''
    =================================
    |    EXAMINATION TABLE          |
    =================================
    | RADIOLOGY {hospital_units["RADIOLOGY"]}
    | HISTOPATHOLOGY {hospital_units["HISTOPATHOLOGY"]}
    | HEMATOLOGY {hospital_units["HEMATOLOGY"]}
    | FERTILITY {hospital_units["FERTILITY"]}
    ==================================
    ''')

    pay_bill = input("\nWhat examination are you paying for: ").upper()
    normal_count()
    patient_pin = pin_1

    if pay_bill in ward_data:
        exam_cost = ward_data[pay_bill]
        print("You're to make payments of", exam_cost, "dollars.")
        deposit_question = input("\nAre you proceding to making payment(yes/no): ").lower()
        normal_count()

        if deposit_question == "yes":
        # Display transaction options
            print(
            '''
            ==============================
            |        SMARTDOC PAY        |
            ==============================
            | 1. Check balance
            | 2. Deposit
            | 3. Check Smartaccount balance
            | 4. Make payment
            | 5. Exit
            ==============================
            ''')

            transaction_choice = int(input("\nSelect transaction(1-5): "))

            if transaction_choice == 2:
                deposit = int(input("\nInput deposit amount:  "))  # in dollars
                normal_count()
                pin_verify = input("Input four digit pin(****): ")
                if pin_verify == patient_pin:
                    print("Deposit of", deposit, "is successful #")     
                    patient_balance += deposit

            elif transaction_choice == 1:
                pin_verify = input("Input four digit pin(****): ")
                if pin_verify == patient_pin:
                    print("Your ledger smartdoc balance is", patient_balance)

            elif transaction_choice == 3:
                print("\nChecking SmartAccount balance...")
                time.sleep(1)
                print("Your SmartAccount balance is", smart_account_balance, "dollars.")

            elif transaction_choice == 4:
                if patient_balance >= exam_cost:
                    pin_verify = input("Input four digit pin(****): ")
                    if pin_verify == patient_pin:
                        patient_balance -= exam_cost
                        # calculate 10% discount to SmartAccount
                        discount = 0.10 * exam_cost
                        smart_account_balance += discount

                        print("\n✅ Payment of", exam_cost, "dollars successful.")
                        print("\n💰 10% Smart discount of", discount, "dollars added to your SmartAccount.")
                        print("\n💳 Remaining balance:", patient_balance)
                        print("\n🏦 SmartAccount balance:", smart_account_balance)
                else:
                    print("⚠️ Insufficient funds! Please deposit more to complete payment.")

            elif transaction_choice == 5:
                print("\nExiting system... Have a nice day, " + patient_name + "!")
                exit()

print(
'''
\t\t\t\t\t=============================
                THANK YOU FOR USING
                    SMARTDOC PAY
\t\t\t\t\t=============================
''')
