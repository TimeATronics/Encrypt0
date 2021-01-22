"""
Caesar Cipher

    Author of Source Code:
                Aradhya Chakrabarti

"""


def caesarEncrypt(message, key):
    encrypted = ''
    for letter in message:
        num = (input_dict_c[letter] + key) % 26
        encrypted += output_dict_c[num]
    return encrypted


def caesarDecrypt(message, key):
    decrypted = ''
    for letter in message:
        num = (input_dict_c[letter] - key + 26) % 26
        decrypted += output_dict_c[num]
    return decrypted


input_dict_c = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
                }

output_dict_c = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
                 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
                 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
                 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'
                 }


def main():

    caesar_message = input("Enter your message here: \n>>>").upper().replace(" ", "")
    key = int(input("Enter your key here: \n>>>"))

    list1 = [i for i in caesar_message if i in input_dict_c.keys()]
    sep = ""
    caesar_message = sep.join(list1)

    encrypted = caesarEncrypt(caesar_message, key)
    decrypted = caesarDecrypt(encrypted, key)

    print("Encrypted Text =", encrypted)
    print("Original Text =", decrypted)


# Executes the main function
if __name__ == '__main__':
    main()
