import argparse
from pathlib import Path
import sys
import textwrap

# -------------------------------------------------------------------------------
# Name:        caesar
# Purpose:     Python module containing Caesar Cipher
#
# Author:      Aradhya Chakrabarti
#
# Created:     17/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------


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

# -------------------------------------------------------------------------------
# Name:        autokey
# Purpose:     Python module containing Autokey Cipher
#
# Author:      Aradhya Chakrabarti
#
# Created:     17/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------


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


# -------------------------------------------------------------------------------
# Name:        decrypt
# Purpose:     Python module containing argparse functions
#
# Author:      Aradhya Chakrabarti
#
# Created:     22/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------

parser = argparse.ArgumentParser(
	prog='encrypt0cli-decrypt.py',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=textwrap.dedent('''\
	\tEncrypt0 CLI Module for decryption:
			Use this program to decrypt an
			encrypted message on the Command Line.
			'''))
parser.add_argument('-file', type=str, help='name of file to be decrypted', required=True)

args = parser.parse_args()

filename = args.file

text = ""
try:
	lines = Path(filename).read_text()
	for i in lines:
		text += i
	text = ''.join(chr(int(s, 2)) for s in text.split())  # taken from bintostr() function
	text = text.split("#@")
except FileNotFoundError:
	print("File not found.\nPlease try again.")
	sys.exit()


def decryptarg(decryptedtxt):
	encrypted_a = text[0]
	key_new = text[1]
	key_c = int(text[2])

	decrypted_c = autokeyDecrypt(encrypted_a, key_new)
	decryptedtxt = caesarDecrypt(decrypted_c, key_c)
	return decryptedtxt


final = decryptarg(text)
print("Decrypted message from the file \"%s\" is:" % str(filename), end="")
print("\n\t" + final)
