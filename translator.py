import characters

class Translator:

    def __init__(self) -> None:
        pass

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
    
    def morseDecoded(message):
        #print (message)
        # 11/29/21 - Currently can take one letter at a time, ie. 'test' in morse is '- . ... -' and is being stored in message as ['-',' ',' .',' ',' .',' .',' .',' ',' -']  
        decoded = []
        letterKeys = list(characters.alphabet.keys())
        letterVals = list(characters.alphabet.values())

        for i in message:
            if i in letterVals:
                getKey = letterVals.index(i)
                decoded.append(letterKeys[getKey])
            else:
                print('not found.')
        print(decoded)