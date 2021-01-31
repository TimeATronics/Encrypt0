import argparse
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
# Name:        encrypt
# Purpose:     Python module containing argparse functions
#
# Author:      Aradhya Chakrabarti
#
# Created:     22/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------

parser = argparse.ArgumentParser(
	prog='encrypt0cli-encrypt.py',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=textwrap.dedent('''\
	Encrypt0 CLI Module for encryption:
		Use this program to encrypt
		a message on the Command Line.
		'''))

parser.add_argument('-file', type=str, help='\
name of new file to put encrypted text into', required=True)
parser.add_argument('-text', type=str, nargs="*", default=None, help='\
text to be encrypted', required=True)
parser.add_argument('-key1', type=str, nargs="*", default=None, help='\
value of LEVEL1 KEY', required=True)
parser.add_argument('-key2', type=int, default=None, help='\
value of LEVEL2 KEY', required=True)

try:
	args = parser.parse_args()
except Exception:
	parser.print_help()
	sys.exit()


def strtobin(string):
	""" Convert Binary String to ASCII Alphabets """
	binary = ' '.join(format(ord(x), 'b') for x in string)
	return binary


def encryptcli(text, key_a, key_c):
	""" Encrypt Message With Entered Keys """
	encrypted_c = caesarEncrypt(text, key_c)
	key_new = full_key(text, key_a)
	encrypted_a = autokeyEncrypt(encrypted_c, key_new)
	return encrypted_a, encrypted_a, key_new


def writeEncryptedcli():
	""" Store Encrypted Message In File """
	try:
		file = open(filename, "wb+")
	except FileNotFoundError:
		print("\nExiting Now")
		sys.exit()
	encrypted_a, encrypted_c, key_new = encryptcli(textdata, key1data, key2data)
	writedata = str(encrypted_a + "#@" + key_new + "#@" + str(key2data))
	writebinary = strtobin(writedata)
	file.write(writebinary.encode("utf-8"))
	file.close()
	print("\nMESSAGE SUCCESSFULLY ENCRYPTED TO FILE")


filename = str(args.file)

if args.text is None or args.text == []:
	print("Enter at least one word for Encryption after \"-text\" argument.")
	sys.exit()
for i in args.text:
	if i.isalpha() is False:
		print("Enter a message having only alphabets or spaces.")
		sys.exit()
else:
	textdata = ''.join([i for i in args.text if i.isalpha()]).upper()


if args.key1 is None or args.key1 == []:
	print("Enter at least one KEY for LEVEL1 encryption.")
	sys.exit()
for i in args.key1:
	if i.isalpha() is False:
		print("Enter a LEVEL1 KEY having only alphabets or spaces.")
		sys.exit()
else:
	key1data = ''.join([i for i in args.key1 if i.isalpha()]).upper()
	if len(key1data) >= len(textdata):
		print("Length of LEVEL1 KEY should be less than %d." % int(len(textdata)))
		sys.exit()


if args.key2 is None or args.key2 not in range(27):
	print("Enter a LEVEL2 KEY in the range(0-26).")
	sys.exit()
else:
	key2data = args.key2


def main():
	""" Main Execution """
	writeEncryptedcli()


if __name__ == '__main__':
	main()
