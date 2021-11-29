import characters

def getCharacters():
    # Create table for alphabet 
    print("{0:5} | {1:^5}".format("Letter", "Morse Character"))
    print("=======================")
    for char in characters.alphabet:
        print("{0:^6} | {1:^6}".format(char,characters.alphabet[str([char][0])]))
    
    # Create table for numbers
    print("{0:5} | {1:^5}".format("Number", "Morse Number"))
    print("=======================")
    for num in characters.numbers:
        print("{0:^6} | {1:^6}".format(num,characters.numbers[str([num][0])]))
    print("")

def morseEncode(word):
    morseWord = []
    for i in word:
        if i in characters.alphabet:
            for x in characters.alphabet:
                if i == x:
                    morseLetter = characters.alphabet[str([i][0])]
                    morseWord.append(morseLetter)
                else:
                    pass
        elif i in characters.numbers:
            for x in characters.numbers:
                if i == x:
                    morseNum = characters.numbers[str([i][0])]
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
            userInput = input("Enter a Letter, Number, Word, or Message: ").lower()
            customList = list(userInput)
            morseEncode(customList)
        elif userChoice == "2":
            getCharacters()
        elif userChoice == "3":
            exit()
        else:
            print("That is not a valid choice.")