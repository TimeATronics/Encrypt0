"""
Autokey Cipher

    Author of Source Code:
                Aradhya Chakrabarti

"""


def full_key(autokey_message, key):
    """Function to create key as long as entered text"""
    i = 0
    while True:
        if len(key) == len(autokey_message):
            break
        elif autokey_message[i] == ' ':
            i += 1
        elif autokey_message[i] not in input_dict_a.keys():
            i += 1
        else:
            key += autokey_message[i]
            i += 1
    return key


def autokeyEncrypt(autokey_message, key_new):
    """Generates encrypted text"""
    i = 0
    encrypted = ''
    for letter in autokey_message:
        x = (input_dict_a[letter] + input_dict_a[key_new[i]]) % 26
        i += 1
        encrypted += output_dict_a[x]
    return encrypted


def autokeyDecrypt(encrypted, key_new):
    """Generates decrypted text"""
    i = 0
    decrypted = ''
    for letter in encrypted:
        x = (input_dict_a[letter] - input_dict_a[key_new[i]] + 26) % 26
        i += 1
        decrypted += output_dict_a[x]
    return decrypted


input_dict_a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
              'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
              'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
              'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
              'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
              }

output_dict_a = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
               5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
               10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
               15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
               20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
               }


def main():
    """Main function for execution"""
    autokey_message = input("Enter your message here: \n>>>").upper().replace(" ", "")
    key = input("Enter your key here: \n>>>").upper().replace(" ", "")

    list1 = [i for i in autokey_message if i in input_dict_a.keys()]
    sep = ""
    autokey_message = sep.join(list1)

    list2 = [i for i in key if i in input_dict_a.keys()]
    key = sep.join(list2)

    key_new = full_key(autokey_message, key)
    encrypted = autokeyEncrypt(autokey_message, key_new)
    decrypted = autokeyDecrypt(encrypted, key_new)

    print("Original Text =", decrypted)
    print("Encrypted Text =", encrypted)


# Executes the main function
if __name__ == '__main__':
    main()
