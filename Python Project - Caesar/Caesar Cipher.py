#Caesar Cipher
#if the key is 3, then A becomes D, B becomes E, C becomes F, and so on.
#translating text into numbers and vice versa

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

print('Do you want to (e)ncrpyt or (d)ecrpyt')
response = input('> ')

if response == 'e': #ENCRYPTION
    print ('Please enter the key (0 to 25) to use.')
    key = int(input ("> "))
    print ('Enter the message to encrypt')
    message = (input ("> ")).upper()
    translation = ''
    for symbol in message:
        if symbol in SYMBOLS: 
            num = SYMBOLS.find(symbol) #Set Character to number
            num = num + key #Difference of Key Value
            if num >= len(SYMBOLS): #Restart the SYMBOLS
                    num = num - len(SYMBOLS)
            translation = translation + SYMBOLS[num]
    print(translation)

if response == 'd': #DECRYPTION
    print ('Please enter the key (0 to 25) to use.')
    key = int(input ("> "))
    print ('Enter the message to decrypt')
    message = (input ("> ")).upper()
    translation = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            translation = translation + SYMBOLS[num]
            if num < 0: #MOVE TO END OF SYMBOLS FOR NEGATIVES
                num = num - len(SYMBOLS) 
    print(translation)
