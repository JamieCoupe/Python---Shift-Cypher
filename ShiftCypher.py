# A shift cipher for encrypting and decrypting a message

# Welcome
print("Welcome to a encrypting and decryption program")

# Initial variables
ctexto = []
ctext = []

ptexto = []
ptext = []

repeat = 0

# Function for encryption
def encryption(factor, message):

    # Get ASCII number for each letter in the message
    for char in message.lower():

        # Add the factor to the number
        ctexto.append((ord(char) - 96) + int(factor) % 26)

    for c in ctexto:
        # Convert number back to letter
        ctext.append(chr(c + 96))

    # Print converted text
    print_text(ctext)



# Function for decryption
def decryption(factor, message):

    # Get ASCII number for each letter in the message
    for char in message.lower():

        # Add factor to the number
        ptexto.append((ord(char) - 96) - int(factor) % 26)

    for c in ptexto:

        # Convert the number back to letter
        ptext.append(chr(c + 96))

    # Print the converted text
    print_text(ptext)

# Printing function
def print_text(text):
    print ("Your message is:", "".join(text))

def repeat_ask():

    # Repeat the whole program?
    ask = input("Do you wish to encode or decode another message (y/n)")

    # Yes answer, return 0 in order to continue break in loop
    if ask.lower() == "y":
        return 0
    # No answer, return 1 in order to end loop
    elif ask.lower() == "n":
        return 1

    # Invalid answer return 0 to continue break in loop
    else:
        print("Please enter Y or N")
        return 0

# Check if the message is only characters
def msg_check(msg):

    # Is all character
    if msg.isalpha():
        return 0

    # Are characters not letters
    else:
        print(" The message is not all letters!", "Please try again.")
        return 1

# Main body of the converter. Repeats over and over
while repeat < 1:

    # Select encrpytion or decryption
    mode = input("Please enter 'en' for encrpytion or 'de' for decryption to select the mode: ")

    # Encryption method
    if mode.lower() == "en":

        # Encryption factor
        fct = input("Please enter a factor between 1 and 26:")
        print ("Factor chosen: " + str(int(fct)% 26))

        # Encryption message
        msg = input("Please enter the string to be encrypted:")

        # Check the message is all characters
        if msg_check(msg) > 0:
            break

        # Call the encryption funciton
        encryption(fct, msg)

        # Repeat the whole process?
        if repeat_ask() > 0:
            print("Thank you for using this program")
            break

        # Clear text lists
        ctexto = []
        ctext = []

    # Decryption method
    elif mode.lower() == "de":

        # Decryption factor
        fct = input("Please enter a factor between 1 and 26:")
        print("Factor chosen: " + str(int(fct) % 26))

        # Decryption message
        msg = input("Please enter the string to be decrypted:")

        # Check the message is all characters
        if msg_check(msg) > 0:
            break

        # Call the decryption function
        decryption(fct, msg)

        # Repeat the whole process?
        if repeat_ask() > 0:
            print("Thank you for using this program")
            break

        # Clear text lists
        ptexto = []
        ptext = []

    # Error in the entered mode
    else:
        print ("no valid mode entered. Please try again.")
