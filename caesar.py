from helpers import alphabet_position, rotate_char
def encrypt_txt(text,rot):
    new_text = ""
    for char in text :
        new_char = rotate_char(char,rot)
        new_text = new_text + new_char
    return(new_text)
def main():
    from sys import argv, exit
    if len(argv) == 1 or argv[1].isalpha():
        print("usage: python caesar.py n")
        exit()
    elif  argv[1].isdigit():
        print("This is what the user typed on the command line:", argv)
        message = input("enter the message to encrypt\n")
        rot_code = int(argv[1])
        print(encrypt(message, rot_code))


if __name__ == "__main__":
    main()


