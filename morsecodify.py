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

def morseEncode(word):
    morseWord = []
    for x in word:
        if x in alphabet:
            for y in alphabet:
                if x == y:
                    morseLetter = alphabet[str([y][0])]
                    morseWord.append(morseLetter)
                else:
                    pass
        elif x in numbers:
            for z in numbers:
                if x == z:
                    morseNum = numbers[str([z][0])]
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
                        "[2] Exit.\n"
                        "> ")

        if userChoice == "1":
            userInput = list(input("Enter a Letter, Number, Word, or Message: "))
            morseEncode(userInput)
        elif userChoice == "2":
            exit()
        else:
            print("That is not a valid choice.")