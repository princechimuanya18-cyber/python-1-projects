# building an age validator for people
# not older than 120 years

print("\t\t--------------------------------\t\t\t")
print("\t\t--------------------------------\t\t\t")
print()
print("\t\t\tWELCOME TO CHIJULY AGE VALIDATOR☺️")
print()
print("\t\t--------------------------------\t\t\t")
print("\t\t--------------------------------\t\t\t")

print("Your name: ") #user's name
name = input(" ")
print()
print("login password:")
password = input(" ") #user's password must have numbers, block and small letters in it

    # Password validation program

# Initialize checks
has_upper = False
has_lower = False
has_digit = False

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Final validation
if has_upper and has_lower and has_digit:
    print("Access granted ✅ Password strength acceptable!")
    print()
    print("Enter your birth year: ")
    age = int(input(" "))

    if age >= 1582:
        if age > 1895:
            print("Congratulations! You have been verified✅")
            print()
                # the user's age is calculated 
            print("Now let's calculate your current age.") 
            print("Enter\"yes\" to proceed:")
            proceed = input(" ")

                #the user was born in the Gregorian calendar and is still abovve 65 years old
            if proceed.lower() == "yes": 
                if 1895 < age <  1960:        
                    print("Woww....You are currently", 2025 - age, "years old, and a kicking elder☺️")
            
                    #final warm greetings
                print("\t\t\t----------------------------") 
                print("\t\t\t----------------------------")   
                print()
                print("\t\t\tTHANK YOU FOR USING CHIJULY AGE VALIDATOR")
                print()
                print("\t\t\t----------------------------") 
                print("\t\t\t----------------------------")   

            else:
                print("Congratulations! Your age is verified✅")

    else:
            print("You appear to be in the Gregorian era, but not valid forr registeration❌")    
            

else:
    print("Access denied ❌ Password must contain at least one uppercase letter, one lowercase letter, and one number.")

