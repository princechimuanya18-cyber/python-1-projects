# creating a 5 x 3 LED display

# a dictionary is built for digits from 0 to 9
digit_dict = {
    "0": [
        "# #",
        "# #",
        "# #",
        "###",
        "# #"
    ],
    "1": [
        "  #",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    "2": [
        " ##",
        " ##",
        " ##",
        " ##",
        " ##"
    ],
    "3": [
        "###",
        "###",
        "# #",
        "# #",
        "# #"
    ],
    "4": [
        "# #",
        "# #",
        "###",
        "# #",
        "# #"
    ],
    "5": [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    "6": [
        "###",
        "###",
        "###",
        "# #",
        "###"
    ],
    "7": [
        "###",
        "# #",
        "###",
        "###",
        "###"
    ],
    "8": [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    "9": [
        "###",
        "###",
        "###",
        "###",
        "###"
    ]
}


number_choice = input("Input digit(s): ")   #user input digit

for row in range(5):
    line = ""
    for digit in number_choice:
        line += digit_dict[digit][row] + " "   # space between digits
    print(line)


if not number_choice.isdigit():
    print("Please input numbers only")
    
    




