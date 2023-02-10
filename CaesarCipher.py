import argparse

if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description = "A CLI tool built with Python 3 designed to encrypt, decrypt, and brute force Caesar Cipher"
    )

    parse.add_argument("-d", help="decryption mode (with known key)", action="store_true")
    parse.add_argument("-b", help="brute force mode (unknown key)", action="store_true")
    parse.add_argument("-e", help="encryption mode", action="store_true")
    parse.add_argument("-t", metavar="--text", help="Enter encrypted or decrypted text")
    parse.add_argument("-k", metavar="--key", help="Enter shit (key) value for decryption mode (-d) or encryption mode (-e)", choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],type=int)

    args = parse.parse_args()

letters = "abcdefghijklmnopqrstuvwxyz"

def encrypt_text(plaintext, n):
    encrypted = ""
    for i in range (len(plaintext)):
        char = plaintext[i]
        shift = letters.find(char.lower())+n

        if shift >= 26:
            shift -= 26
        if char == " ":
            encrypted+=" "
        elif(not char.isalpha()):
            encrypted+=char
        elif(char.isupper()):
            encrypted+=letters[shift].upper()
        else:
            encrypted+=letters[shift].lower()
    return encrypted

def decrypt_text(encrypted, n):
    decrypted = ""
    for i in range (len(encrypted)):
        char = encrypted[i]
        shift = letters.find(char.lower())-n

        if shift >= 26:
            shift -= 26
        if char == " ":
            decrypted+=" "
        elif(not char.isalpha()):
            decrypted+=char
        elif(char.isupper()):
            decrypted+=letters[shift].upper()
        else:
            decrypted+=letters[shift].lower()
    return(decrypted)

def decrypt_text_brute(message):
    message = message.lower()
    for key in range(len(letters)):
        translated = ''
        for char in message:
            if char in letters:
                num = letters.find(char)
                num -= key
                if num < 0:
                    num += len(letters)
                translated += letters[num]
            else:
                translated += char
        print('Key: %s - %s' % (key, translated))

if (args.d): # decrypt_text
    print(decrypt_text(args.t, args.k))
elif (args.b): # decrypt_text_brute
    decrypt_text_brute(args.t)
elif (args.e): # encrypt_text
    print(encrypt_text(args.t, args.k))