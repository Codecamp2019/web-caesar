def alphabet_position(char):
    cipher_code = "abcdefghijklmnopqrstuvwxyz"
    char = char.lower()
    pos = cipher_code.find(char)
    return(pos)

def rotate_char(char, rot):
    caesar_cipher_lower = "abcdefghijklmnopqrstuvwxyz"
    caesar_cipher_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = """!@#$%^&*'"(){}|:?><;/.- +=\, \~"""
    numbers = "0123456789"
    if char in special_chars or char in numbers:
        return(char)
    elif char in caesar_cipher_lower:
            pos = alphabet_position(char)
            new_pos = (pos + rot) % 26
            return(caesar_cipher_lower[new_pos])
    elif char in caesar_cipher_upper:
            pos = alphabet_position(char)
            new_pos = (pos + rot) % 26
            return(caesar_cipher_upper[new_pos])
