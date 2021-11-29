from translator import Translator

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
                        "[2] Enter a Morse Code message to be translated.\n"
                        "[3] View Characters.\n"
                        "[4] Exit.\n"
                        "> ")

        if userChoice == "1":
            userInput = input("Enter a Letter, Number, Word, or Message: ").lower()
            customList = list(userInput)
            Translator.morseEncode(customList)
        elif userChoice == "2":
            encodedInput = str(input("Enter your Morse Code letter, number, or message: "))
            encodedList = list(encodedInput)
            Translator.morseDecoded(encodedList)
        elif userChoice == "3":
            Translator.getCharacters()
        elif userChoice == "4":
            exit()
        else:
            print("That is not a valid choice.")