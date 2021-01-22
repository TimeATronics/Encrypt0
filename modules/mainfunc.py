# -------------------------------------------------------------------------------
# Name:        mainfunc
# Purpose:     Python module containing all main function definitions
#
# Author:      Aradhya Chakrabarti
#
# Created:     18/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------

from modules.auxfunc import *
import modules.autokey
import modules.caesar
import os
import sys
import time


width = os.get_terminal_size().columns  # width of terminal (for .center method)


def inputMessage():
	"""Function for taking input of message to be encrypted"""
	global message
	global length
	while True:
		try:
			message = input("\n\tEnter your message here:\n\t>>>").upper().replace(" ", "")
		except ValueError:
			print("\tMessage should only contain alphabets or spaces.")
		except KeyboardInterrupt:
			print("\n")
			pass
		else:
			if message.isalpha() is False:
				print("\tMessage should only contain alphabets or spaces.")
			else:
				break
	# To remove all other elements in input than alphabets.
	list1 = [i for i in message if i in modules.caesar.input_dict_c.keys()]
	sep = ""
	message = sep.join(list1)
	length = len(message)


def inputKeyA():
	""" Function for taking input of KEY_LEVEL1 """
	global key_a
	inputtext1 = "\n\tEnter a key for LEVEL1 encryption (only alphabets allowed)\n\t>>>"
	while True:
		try:
			key_a = input(inputtext1).upper().replace(" ", "")
		except ValueError:
			print(f"\tPlease enter a valid Key (length < {length})")
		except KeyboardInterrupt:
			print("\n")
			pass
		else:
			if key_a.isalpha() is False or len(key_a) >= length:
				print(f"\tPlease enter a valid Key (length < {length})")
			else:
				break
	# To remove all other elements in key_a than alphabets.
	list2 = [i for i in key_a if i in modules.autokey.input_dict_a.keys()]
	sep = ""
	key_a = sep.join(list2)


def inputKeyC():
	""" Function for taking input of KEY_LEVEL2 """
	global key_c
	while True:
		try:
			key_c = +int(input("\n\tEnter a key for LEVEL2 (only integers allowed)\n\t>>>"))
		except ValueError:
			print("\tPlease enter a integer between 0 and 26")
		except KeyboardInterrupt:
			print("\n")
			pass
		else:
			if key_c not in range(27):
				print("\tPlease enter a integer between 0 and 26")
			else:
				break


def keyCGlobal():
	""" Function for making key_c available to main.py """
	return key_c


def inputSuffix():
	""" Function to input suffix for data{{suffix}}.bin (foor encryption) """
	# This is a normal returnable function called inside writeEncrypted()

	try:
		suffix = int(input("\n\tEnter an integer suffix for new filename\n\t>>>"))
	except ValueError:
		print("\tPlease enter an integer value")
		print("\n\tTry again next time.")
		print("Exiting Now".center(width))
		time.sleep(3)
		clearScreen()
		sys.exit()
	except KeyboardInterrupt:
		print("\n")
		pass
	else:
		return suffix


def inputDSuffix1():
	""" Function to input suffix for data{{suffix}}.bin (for decryption) """
	# This variable is global since decrypt function is called in writeDecrypted
	# Hence is this function is calles in writeDecrypted,
	# Loop of calls would be made.

	global dsuffix1

	try:
		dsuffix1 = int(input("\n\tEnter desired integer suffix for data{{suffix}}.bin\n\t>>>"))
	except ValueError:
		print("\tPlease enter an integer value")
		print("\n\tTry again next time.")
		print("Exiting Now".center(width))
		time.sleep(3)
		clearScreen()
		sys.exit()
	except KeyboardInterrupt:
		print("\n")
		pass


def inputDSuffix2():
	""" Function to input suffix for decrypted{{suffix}}.txt """
	# This variable is global since decrypt function is called in writeDecrypted
	# Hence is this function is calles in writeDecrypted,
	# Loop of calls would be made.

	global dsuffix2

	try:
		dsuffix2 = int(input("\n\tEnter an integer suffix for new file (decrypted{{suffix}}.txt)\n\t>>>"))
	except ValueError:
		print("\tPlease enter an integer value")
		print("\n\tTry again next time.")
		print("Exiting Now".center(width))
		time.sleep(3)
		clearScreen()
		sys.exit()
	except KeyboardInterrupt:
		print("\n")
		pass


def strtobin(string):
	""" Convert string to binary string for encrypt() """
	binary = ' '.join(format(ord(x), 'b') for x in string)
	return binary


def bintostr(binary):
	""" Convert binary string to ascii string for decrypt() """
	string = ''.join(chr(int(s, 2)) for s in binary.split())
	return string


class EnDProcess:
	""" Main Encryption and Decryption Functions """

	global decrypted

	def __init__(self, message, key_a, key_c):
		self.message = message
		self.key_a = key_a
		self.key_c = key_c

	def encrypt(self):
		""" Using cipher module functions to encrypt message """

		encrypted_c = modules.caesar.caesarEncrypt(message, key_c)
		key_new = modules.autokey.full_key(message, key_a)
		encrypted_a = modules.autokey.autokeyEncrypt(encrypted_c, key_new)

		return encrypted_c, encrypted_a, key_new

	def writeEncrypted(self, encrypted_a, key_new, key_c):
		""" Function to write encrypted message + "#@" ... to data{{suffix}}.bin """

		suffix = inputSuffix()
		data_filename = f'data{suffix}.bin'

		try:
			file = open('.\\user\\%s' % data_filename, "wb+")
		except FileNotFoundError:
			print("\tFile and/or directory not found.")
			print("\n\tTry again next time.")
			print("Exiting Now".center(width))
			time.sleep(3)
			clearScreen()
			sys.exit()
		except KeyboardInterrupt:
			print("\n")
			pass

		writedata = str(encrypted_a + "#@" + key_new + "#@" + str(key_c))

		writebinary = strtobin(writedata)  # convert writedata to binary "string"

		file.write(writebinary.encode("utf-8"))  # write binary "string" as utf-8
		file.close()

		print("MESSAGE SUCCESSFULLY ENCRYPTED TO FILE".center(width))
		time.sleep(2)

	def decrypt(self):
		""" Function to read and decrypt data from ~.data after splitting terms """

		global decrypted

		data_filename = f'data{dsuffix1}.bin'

		try:
			file = open('.\\user\\%s' % data_filename, "rb")
		except FileNotFoundError:
			print("\tFile and/or directory not found.")
			print("\n\tTry again next time.")
			print("Exiting Now".center(width))
			time.sleep(3)
			clearScreen()
			sys.exit()
		except KeyboardInterrupt:
			print("\n")
			pass

		data = file.read()
		data_decode = bintostr(data)  # convert "data" to ascii mapping
		file.close()

		list_data = data_decode.split("#@")  # splitting the string w.r.t #@
		encrypted_a = list_data[0]
		key_new = list_data[1]
		key_c = int(list_data[2])

		decrypted_c = modules.autokey.autokeyDecrypt(encrypted_a, key_new)
		decrypted = modules.caesar.caesarDecrypt(decrypted_c, key_c)
		return decrypted

	def writeDecrypted(self, decrypted):
		""" Function to write decrypted text to decrypted.txt """

		decrypted_filename = f'decrypted{dsuffix2}.txt'

		try:
			file = open('.\\user\\%s' % decrypted_filename, "wb+")
		except Exception:
			pass
		except KeyboardInterrupt:
			print("\n")
			pass
		else:
			if os.path.isdir('.\\user\\'):
				pass
			else:
				print("\tFile and/or directory not found.")
				print("\n\tTry again next time.")
				print("Exiting Now".center(width))
				time.sleep(3)
				clearScreen()
				sys.exit()

		file = open('.\\user\\%s' % decrypted_filename, "w")
		file.write(decrypted)
		file.close()
		print("MESSAGE SUCCESSFULLY DECRYPTED TO FILE".center(width))
		time.sleep(2)


if __name__ == '__main__':
	# main()
	pass
