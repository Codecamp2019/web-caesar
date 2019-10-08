from helpers import alphabet_position, rotate_char
from caesar import encrypt
def vigenere(text,encryption_key):
    encrypt_code_list = []
    encrypt_text = ""
    for char in encryption_key:
        encrypt_code_list.append(alphabet_position(char))
    i = 0
    for char in text :
        if char == encrypt(char, encrypt_code_list[i]):
            encrypt_text = encrypt_text + char
        else: 
            encrypt_text = encrypt_text + encrypt(char, encrypt_code_list[i])
            i = i + 1
        if i == (len(encrypt_code_list)):
            i = 0
    return(encrypt_text)

def main():
    from sys import argv, exit
    if len(argv) == 1 :
        print("usage: python vigenere.py keyword: ")
        exit()
    if argv[1].isdigit():
        print("""-keyword : The string to be used as a "key" to encrypt 
        your message. Should only contain alphabetic characters--
         no numbers or special characters.""")
        exit()
    elif argv[1].isalpha():
        message = input("Type the message:\n")
        print(vigenere(message, argv[1] ))

       

if __name__ == "__main__":
    main()

    