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
userinput = input('Enter a letter or number: ')

# Check to see if user input is a letter or number, and find within the dictionaries
if userinput in alphabet:
    for i in alphabet:
        if i == userinput:
            print(alphabet[str([i][0])])
        else:
            pass
elif userinput in numbers:
    for i in numbers:
        if i == userinput:
            print(numbers[str([i][0])])
        else:
            pass
else:
    print('Not found!')

# User enters a word or sentence and then gets constructed in Morse Code
userWord = list(input('Enter a word or message: '))
morseWord = []
for x in userWord:
    for y in alphabet:
        if x == y:
            morseLetter = alphabet[str([y][0])]
            morseWord.append(morseLetter)

print('Your message in Morse Code: ',*morseWord)