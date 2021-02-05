# ---------------------------------------------------------------------
# Name:        decrypt
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

import sys
import textwrap
import string
import argparse
from pathlib import Path


def caesarDecrypt(message, key):
	decrypted = ''
	for letter in message:
		num = (input_dict_c[letter] - key + 26) % 26
		decrypted += output_dict_c[num]
	return decrypted


input_dict_c = {key: i + 1 for i, key in enumerate([i for i in string.ascii_uppercase])}
output_dict_c = {i + 1: key for i, key in enumerate([i for i in string.ascii_uppercase[0:25]])}
output_dict_c[0] = 'Z'


def autokeyDecrypt(encrypted, key_new):
	"""Generates decrypted text"""
	i = 0
	decrypted = ''
	for letter in encrypted:
		x = (input_dict_a[letter] - input_dict_a[key_new[i]] + 26) % 26
		i += 1
		decrypted += output_dict_a[x]
	return decrypted


input_dict_a = {key: i for i, key in enumerate([i for i in string.ascii_uppercase])}
output_dict_a = {i: key for i, key in enumerate([i for i in string.ascii_uppercase])}

parser = argparse.ArgumentParser(
	prog='decrypt',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=textwrap.dedent('''\
	\tEncrypt0 CLI Module for decryption:
			Use this program to decrypt an
			encrypted message on the Command Line.
			'''))
parser.add_argument('-file', type=str, help='name of file to be decrypted', required=True)

try:
	args = parser.parse_args()
except Exception:
	parser.print_help()
	sys.exit()

filename = str(args.file)

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
