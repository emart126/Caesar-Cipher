# author: Eric Martinez
# file: cipher.py is a program that decodes and encodes ASCII text, given by the user, through a caesar cipher


# read text from a file and return text as a string
# the function should contain an input statement, open file statement,
# and try-except statement
def readfile():
    message = ""
    

    while (True):
        inputFile = input("Please enter a file for reading:")

        try:
            file1 = open(inputFile, "r")
            message = file1.read()
            break
        except IOError:
            print("File can't be oppened!")
            continue
        else:
            file1.close()
        
    return message


# write a string (message) to a file
# the function should contain an input statement, open file statement,
# and try-except statement
def writefile(message):
    inputFile = input("Please enter a file for writing:")
    try:
        file1 = open(inputFile, "w")
        file1.write(message)
        
    except IOError:
        print("File can't be opened!")
    else:
        file1.close()


# make a list (tuple) of letters in the English alphabet
def make_alphabet():
    alphabet = ()
    for i in range(26):
        char = i + 65
        alphabet += (chr(char), )
    return alphabet


# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
    plaintext = plaintext.upper()
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return to_string(ciphertext)


# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(text):
    text = text.upper()
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in text:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)

    return to_string(plaintext)


# convert a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the string "HOW ARE YOU?"
def to_string(text):
    s = ""
    for character in text:
        s += character
    return s


# main program
menu = "Would you like to encode or decode the message?\nType E to encode, D to decode, or Q to quit"
choice = ''

while (True):
    print(menu)
    choice = input().upper()
    if (choice == 'E'):
        userFile = readfile()
        encodedText = encode(userFile)
        writefile(encodedText)

        print(f"Plaintext:\n{userFile}\nCiphertext:\n{encodedText}")
        
    elif (choice == 'D'):
        userFile = readfile()
        decodedText = decode(userFile)
        writefile(decodedText)

        print(f"Ciphertext:\n{userFile}\nPlaintext:\n{decodedText}")

    elif (choice == 'Q'):
        break
    else:
        print("You did not choose correctly.")
        continue
print("Goodbye!")
