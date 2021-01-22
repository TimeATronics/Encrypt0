# -------------------------------------------------------------------------------
# Name:        main
# Purpose:     Main Python module for execution
#
# Author:      Aradhya Chakrabarti
#
# Created:     18/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------

from modules.mainfunc import *
from modules.auxfunc import *
import os
import time


width = os.get_terminal_size().columns


def startEncryptionProcess():
	"""Create instance of EnDProcess to call encrypt function"""
	# Taking all input:
	StartEncrypt = EnDProcess(message=inputMessage(), key_a=inputKeyA(), key_c=inputKeyC())
	# Call to encrypt function:
	StartEncrypt.encrypt()
	# Assigning returned values from returned values:
	encrypted_c, encrypted_a, key_new = StartEncrypt.encrypt()
	key_c = keyCGlobal()
	# Writing encrypted data to data.bin:
	# inputFilemname_data()
	StartEncrypt.writeEncrypted(encrypted_a, key_new, key_c)


def startSequence():
	""" Function to arrange other functions in starting sequence"""
	clearScreen()
	sleep_global()
	loadingScreen()


def startScreen():
	""" Function to display icon and startup text """
	pyfiglet_icon()
	choicelist = "\n\t<ENCRYPT>(1)\t<DECRYPT>(2)\t<EXIT>(3)\t<VIEW HELP>(4)?"
	print("Hello and welcome to ENCRYPT0".center(width))
	print("\tThis is a program written in Python to help you encrypt small messages.")
	print("\tThis program can encrypt any alphabetical message you provide.\n")
	print("\t\tTo encrypt a message, press <1>\n")
	print("\tYou can also decrypt a message initially encrypted with this tool.")
	print("\t\tTo decrypt an encrypted message, press <2>\n")
	print("\tBefore choosing to decrypt, make sure that")
	print("\tthe file containing the encrypted text (data{{suffix}}.bin)")
	print("\tis already present in the \"user\" directory inside the working directory.")
	print("\n\tTo exit the program, press <3> when the option is present.\n")
	print("\n\tFinally, <4> press again when you require to view this text again.\n")
	print("\n\nWould you like to:\n".center(width), choicelist)


def startHelp():
	""" Function to display same help text """
	print("\tThis program can encrypt any alphabetical message you provide.")
	print("\t\tTo encrypt a message, press <1>\n")
	print("\tYou can also decrypt a message initially encrypted with this tool.")
	print("\t\tTo decrypt an encrypted message, press <2>\n")
	print("\tBefore choosing to decrypt, make sure that")
	print("\tthe file containing the encrypted text (data.bin)")
	print("\tis already present in the \"user\" directory inside the working directory.\n")
	print("\t\tTo exit the program, press <3> when the option is present.\n")
	print("\t\tFinally, <4> press again when you require to view this text again.")


def startScreenInput():
	""" Function to take input in main window """
	global choice
	while True:
		try:
			choice = int((input(">>>")).replace(" ", ""))
		except ValueError:
			print("\tPlease enter a valid integer between 1 & 4")
		except KeyboardInterrupt:
			print("\n")
			pass
		else:
			if choice not in (1, 2, 3, 4):
				print("\tPlease enter a valid integer between 1 & 4")
				continue
			else:
				break


def startDecryptionProcess():
	""" Function to create instance of EnDProcess and call decrypt function """
	StartDecrypt = EnDProcess(message="", key_a="", key_c="")
	inputDSuffix1()
	StartDecrypt.decrypt()
	inputDSuffix2()
	StartDecrypt.writeDecrypted(StartDecrypt.decrypt())


def main():
	""" Main function which is executed """
	# This loop is to enable user input after any one process and not abruptly exit.
	while True:
		try:
			startSequence()
			startScreen()
			startScreenInput()

			if choice == 1:
				loadingScreen()
				pyfiglet_icon()
				startEncryptionProcess()
				time.sleep(1)

			elif choice == 2:
				loadingScreen()
				pyfiglet_icon()
				startDecryptionProcess()
				time.sleep(1)

			elif choice == 3:
				print("Exiting Now".center(width))
				sleep_global()
				clearScreen()
				sys.exit()

			elif choice == 4:
				startHelp()
				pass
		except KeyboardInterrupt:
			pass


if __name__ == '__main__':
	main()
