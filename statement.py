number = int(input("Enter a number between 1-10): "))

number_2 = float(input("Enter second number: "))

if number_2 == number:
    try:
        print("You\'re right")
    except:
        print("You\'re wrong")


