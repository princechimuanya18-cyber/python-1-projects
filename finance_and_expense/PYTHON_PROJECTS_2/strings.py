multiline = """Gas #1
food #2"""

print(len(multiline))

multi = """Eagle @23
blessings @24"""

operation = """Kite @15
chick @25"""
import time
print(len(multi + operation))

name = input("Enter your name: ")
print("procesing..")
time.sleep(1)

classes = int(input("Enter wallet address balance: "))

name *= classes
print(name)


text = "Hello 👋"
encoded_bytes = text.encode('utf-8')
print(f"Encoded bytes: {encoded_bytes}")
decoded_text = encoded_bytes.decode('utf-8')
print(f"Decoded text: {decoded_text}")

print('[' + "great".center(10, "-") + ']')

x = ['boy', 'girl', 'wallet']
y = [2, 4, 6, 8]


x.extend(y)
print(x)
y = sorted(y)
print(y)

y.sort()
print(y)
y = sorted(y, reverse=True)
print(y)
y.sort(reverse=True)
print(y)



import string

password = input("Enter your password (must contain upper, lower, number, and special characters): ")

special_chars = string.punctuation

# Check for at least one letter
has_letter = any(char.isalpha() for char in password)

# Check for at least one number
has_number = any(char.isdigit() for char in password)

# Check for at least one special character
has_special_char = any(char in special_chars for char in password)

if has_letter and has_number and has_special_char:
    print("Password verified")
else:
    print("Invalid password")


names = ["KELVIN", "MAN", "Beloveth"]

names_1 = " Belarin"
names_2 = "Merlin in the shaadows"

name = ".".join(names)
print(name)

name_1a = names_1.lstrip()
print(name_1a)

name_2a = name_1a.lstrip("Be")
print(name_2a)

names_final = names_2.replace("the", "at")
print(names_final)

#making my function act like a split method
def mysplit(strng):
    listing = []
    space = ""

    for char in strng:
        if char != " ":
            space += char
        else:
            if space != "":
                listing.append(space)
                space = ""

    if space != "":
        listing.append(space)
    
    return listing
        
    
print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

