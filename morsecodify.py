alphabet = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    ' ':'  '        # for spaces
}
numbers = {
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----'
}

def getCharacters():
    # Create table for alphabet 
    print("{0:5} | {1:^5}".format("Letter", "Morse Character"))
    print("=======================")
    for char in alphabet:
        print("{0:^6} | {1:^6}".format(char,alphabet[str([char][0])]))
    
    # Create table for numbers
    print("{0:5} | {1:^5}".format("Number", "Morse Number"))
    print("=======================")
    for num in numbers:
        print("{0:^6} | {1:^6}".format(num,numbers[str([num][0])]))
    print("")

def morseEncode(word):
    morseWord = []
    for i in word:
        if i in alphabet:
            for x in alphabet:
                if i == x:
                    morseLetter = alphabet[str([i][0])]
                    morseWord.append(morseLetter)
                else:
                    pass
        elif i in numbers:
            for x in numbers:
                if i == x:
                    morseNum = numbers[str([i][0])]
                    morseWord.append(morseNum)
                else:
                    pass
        else:
            print("Could not translate.")
    # Return the user input as Morse Code
    print('Your message in Morse Code: ',*morseWord)

if __name__ == '__main__':
    
    print("___  ___                      _____           _ _  __       ")
    print("|  \/  |                     /  __ \         | (_)/ _|      ")
    print("| .  . | ___  _ __ ___  ___  | /  \/ ___   __| |_| |_ _   _ ")
    print("| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` | |  _| | | |")
    print("| |  | | (_) | |  \__ \  __/ | \__/\ (_) | (_| | | | | |_| |")
    print("\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|_|_|  \__, |")
    print("     -- --- .-. ... .    -.-. --- -.. .. ..-. -.--     __/ |")
    print("                                                      |___/ \n")

    while True:
        userChoice = input("Make a selection below to continue.\n"
                        "[1] Enter a message to translate to Morse Code.\n"
                        "[2] View Characters.\n"
                        "[3] Exit.\n"
                        "> ")

        if userChoice == "1":
            userInput = list(input("Enter a Letter, Number, Word, or Message: "))
            morseEncode(userInput)
        elif userChoice == "2":
            getCharacters()
        elif userChoice == "3":
            exit()
        else:
            print("That is not a valid choice.")