# ---------------------------------------------------------------------
# Name:        encrypt
# Author:      Aradhya Chakrabarti

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------

import argparse
import sys
import textwrap
import string


def caesarEncrypt(message, key):
	encrypted = ''
	for letter in message:
		num = (input_dict_c[letter] + key) % 26
		encrypted += output_dict_c[num]
	return encrypted


input_dict_c = {key: i + 1 for i, key in enumerate([i for i in string.ascii_uppercase])}
output_dict_c = {i + 1: key for i, key in enumerate([i for i in string.ascii_uppercase[0:25]])}
output_dict_c[0] = 'Z'


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


input_dict_a = {key: i for i, key in enumerate([i for i in string.ascii_uppercase])}
output_dict_a = {i: key for i, key in enumerate([i for i in string.ascii_uppercase])}

parser = argparse.ArgumentParser(
	prog='encrypt',
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
	return encrypted_a, key_new


def writeEncryptedcli():
	""" Store Encrypted Message In File """
	try:
		file = open(filename, "wb+")
	except FileNotFoundError:
		print("\nExiting Now")
		sys.exit()
	encrypted_a, key_new = encryptcli(textdata, key1data, key2data)
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

if __name__ == '__main__':
	writeEncryptedcli()
