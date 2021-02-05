# ---------------------------------------------------------------------
# Name:        Encrypt0
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

import subprocess
import platform
import string
import os
import sys
from time import sleep
from pyfiglet import figlet_format
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

# Instance of Console class from rich.console
console = Console()

# nt == Windows, posix == unix
try:
	if os.name == 'nt':
		userfolder = ".\\user\\"
	elif os.name == 'posix':
		userfolder = "./user/"
except Exception:
	userfolder = "."
	pass


# Caesar Cipher:
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


# A: 1 to Z: 26
input_dict_c = {key: i + 1 for i, key in enumerate([i for i in string.ascii_uppercase])}
# A: 1 to Y: 25 and Z: 0
output_dict_c = {i + 1: key for i, key in enumerate([i for i in string.ascii_uppercase[0:25]])}
output_dict_c[0] = 'Z'


# Autokey Cipher:
def full_key(autokey_message, key):
	i = 0
	while True:
		if len(key) == len(autokey_message):
			break
		else:
			key += autokey_message[i]
			i += 1
	return key


def autokeyEncrypt(autokey_message, key_new):
	i = 0
	encrypted = ''
	for letter in autokey_message:
		x = (input_dict_a[letter] + input_dict_a[key_new[i]]) % 26
		i += 1
		encrypted += output_dict_a[x]
	return encrypted


def autokeyDecrypt(encrypted, key_new):
	i = 0
	decrypted = ''
	for letter in encrypted:
		x = (input_dict_a[letter] - input_dict_a[key_new[i]] + 26) % 26
		i += 1
		decrypted += output_dict_a[x]
	return decrypted


# A: 0 B:1 to Z: 25
input_dict_a = {key: i for i, key in enumerate([i for i in string.ascii_uppercase])}
# # 0: A to 25: Z
output_dict_a = {i: key for i, key in enumerate([i for i in string.ascii_uppercase])}


def clearScreen():
	if platform.system() == "Windows":
		subprocess.Popen("cls", shell=True).communicate()
	else:
		print("\033c", end="")


def printDir(dir):
	try:
		if os.path.isdir(userfolder):
			print("\n\tThe %s Directory contains:\n" % dir)
			for root, dirs, files in os.walk(dir):
				level = root.replace(dir, '').count(os.sep)
				indent = '| ' * level
				print('\t\t{}{} \\\n'.format(indent, os.path.basename(root)))
				subindent = '| ' * (level + 1)
				for f in files:
					print('\t\t{}{}\n'.format(subindent, f))
		else:
			fileNotFoundErrorMessage()
	except FileNotFoundError:
		fileNotFoundErrorMessage()
	except KeyboardInterrupt:
		console.print("\n")
		pass


def pyfiglet_icon():
	result = figlet_format("Encrypt0", font="bulbhead", justify="center")
	return result


def loadingScreen():
	clearScreen()
	print("Loading:")
	animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
				 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
				 "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"
				 ]
	for i in range(len(animation)):
		sleep(0.2)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()
	print("\n")
	clearScreen()


def fileNotFoundErrorMessage():
	console.print("\tFile and/or directory not found.", style="b red")
	console.print("\n\tTry again next ", style="b red")
	console.print("Exiting Now", justify="center", style="b red")
	sleep(3)
	clearScreen()
	sys.exit()


def valueErrorMessage():
	console.print("\tPlease enter an integer value", style="b red")
	console.print("\n\tTry again next ", style="b red")
	console.print("Exiting Now", justify="center", style="b red")
	sleep(3)
	clearScreen()
	sys.exit()


def inputMessage():
	""" Main message input """
	global message
	global length
	while True:
		try:
			console.print("\n\tEnter your message here:\
\n\t[bold red]>>>[/bold red] ", style="b green", end="")
			message = input().upper().replace(" ", "")
		except ValueError:
			console.print("\tMessage should only contain alphabets or spaces.", style="red b")
		except KeyboardInterrupt:
			console.print("\n")
			pass
		else:
			if message.isalpha() is False:
				console.print("\tMessage should only contain alphabets or spaces.", style="b red")
			else:
				break
	list1 = [i for i in message if i in input_dict_c.keys()]
	message = "".join(list1)
	length = len(message)


def inputKeyA():
	""" KEY1 Input """
	global key_a
	while True:
		try:
			console.print("\n\tEnter a key for LEVEL1 encryption \
(only alphabets allowed): \n\t[bold red]>>> [/bold red]", style="b green", end="")
			key_a = input().upper().replace(" ", "")
		except ValueError:
			console.print(f"\tPlease enter a valid Key (length < {length})", style="b red")
		except KeyboardInterrupt:
			console.print("\n")
			pass
		else:
			if key_a.isalpha() is False or len(key_a) >= length:
				console.print(f"\tPlease enter a valid Key (length < {length})", style="b red")
			else:
				break
	list2 = [i for i in key_a if i in input_dict_a.keys()]
	key_a = "".join(list2)


def inputKeyC():
	""" KEY2 Input """
	global key_c
	while True:
		try:
			console.print("\n\tEnter a key for LEVEL2 encryption \
(only positive integers allowed): \n\t[bold red]>>> [/bold red]", style="b green", end="")
			key_c = +int(input())
		except ValueError:
			console.print("\tPlease enter a integer between 0 and 26", style="b red")
		except KeyboardInterrupt:
			console.print("\n")
			pass
		else:
			if key_c not in range(27):
				console.print("\tPlease enter a integer between 0 and 26", style="b red")
			else:
				break


def inputSuffix():
	""" data.bin suffix input during encryption """
	try:
		console.print("\n\tEnter an integer suffix for \
new filename\n\t[bold red]>>> [/bold red]", style="b green", end="")
		suffix = int(input())
	except ValueError:
		valueErrorMessage()
	except KeyboardInterrupt:
		console.print("\n")
		pass
	else:
		return suffix


def inputDSuffix1():
	""" decrypted.txt suffix input during decryption """
	global dsuffix1
	try:
		console.print("\n\tEnter desired integer suffix for \
data{{suffix}}.bin\n\t[bold red]>>> [/bold red]", style="b green", end="")
		dsuffix1 = int(input())
	except ValueError:
		valueErrorMessage()
	except KeyboardInterrupt:
		console.print("\n")
		pass


def inputDSuffix2():
	""" data.bin suffix input during decryption """
	global dsuffix2
	try:
		console.print("\n\tEnter an integer suffix for new \
file (decrypted{{suffix}}.txt)\n\t[bold red]>>> [/bold red]", style="b green", end="")
		dsuffix2 = int(input())
	except ValueError:
		valueErrorMessage()
	except KeyboardInterrupt:
		console.print("\n")
		pass


def strtobin(string):
	""" Convert ASCII string to Binary string """
	binary = ' '.join(format(ord(x), 'b') for x in string)
	return binary


def bintostr(binary):
	""" Convert Binary string to ASCII string """
	string = ''.join(chr(int(s, 2)) for s in binary.split())
	return string


class EnDProcess:
	""" All encryption and decryption process definitions """
	global decrypted

	def __init__(self, message, key_a, key_c):
		self.message = message
		self.key_a = key_a
		self.key_c = key_c

	def encrypt(self):
		encrypted_c = caesarEncrypt(message, key_c)
		key_new = full_key(message, key_a)
		encrypted_a = autokeyEncrypt(encrypted_c, key_new)
		return encrypted_c, encrypted_a, key_new

	def writeEncrypted(self, encrypted_a, key_new, key_c):
		suffix = inputSuffix()
		data_filename = f'data{suffix}.bin'
		try:
			file = open(userfolder + data_filename, "wb+")
		except FileNotFoundError:
			fileNotFoundErrorMessage()
		except KeyboardInterrupt:
			console.print("\n")
			pass
		writedata = str(encrypted_a + "#@" + key_new + "#@" + str(key_c))
		writebinary = strtobin(writedata)
		file.write(writebinary.encode("utf-8"))
		file.close()
		console.print("MESSAGE SUCCESSFULLY ENCRYPTED TO FILE", justify="center", style="b magenta")
		sleep(2)

	def decrypt(self):
		global decrypted
		data_filename = f'data{dsuffix1}.bin'
		try:
			file = open(userfolder + data_filename, "rb")
		except FileNotFoundError:
			fileNotFoundErrorMessage()
		except KeyboardInterrupt:
			console.print("\n")
			pass
		data = file.read()
		data_decode = bintostr(data)
		file.close()
		list_data = data_decode.split("#@")
		encrypted_a = list_data[0]
		key_new = list_data[1]
		key_c = int(list_data[2])
		decrypted_c = autokeyDecrypt(encrypted_a, key_new)
		decrypted = caesarDecrypt(decrypted_c, key_c)
		return decrypted

	def writeDecrypted(self, decrypted):
		decrypted_filename = f'decrypted{dsuffix2}.txt'
		try:
			file = open(userfolder + decrypted_filename)
		except Exception:
			pass
		except KeyboardInterrupt:
			console.print("\n")
			pass
		else:
			if os.path.isdir(userfolder):
				pass
			else:
				fileNotFoundErrorMessage()
		file = open(userfolder + decrypted_filename, "w")
		file.write(decrypted)
		file.close()
		console.print("MESSAGE SUCCESSFULLY DECRYPTED TO FILE", justify="center", style="b magenta")
		sleep(2)


# Main execution functions from here onward:

def startEncryptionProcess():
	StartEncrypt = EnDProcess(message=inputMessage(), key_a=inputKeyA(), key_c=inputKeyC())
	StartEncrypt.encrypt()
	encrypted_c, encrypted_a, key_new = StartEncrypt.encrypt()
	StartEncrypt.writeEncrypted(encrypted_a, key_new, key_c)


def startScreen():
	icon = pyfiglet_icon()
	console.print(icon, style="red b")
	console.print("\nWelcome to ENCRYPT0", justify="center", style="b cyan")
	console.print("This is a program written in Python to help \n\
you encrypt small alphabetical messages.\n", justify="center", style="b green")
	console.print("\nType one of these choices into the \
prompt to continue.", justify="center", style="b cyan")


def startHelp():
	""" Read README.md and print it on terminal """
	try:
		readme = open("README_TUI.md", encoding="utf-8")
		markdown = Markdown(readme.read())
		console.print(markdown)
	except FileNotFoundError:
		fileNotFoundErrorMessage()
	except KeyboardInterrupt:
		console.print("\n")
		pass


def startScreenInput():
	""" Input for main dashboard """
	global choice
	while True:
		try:
			console.print(">>> ", style="b red", end="")
			choice = int((input()).replace(" ", ""))
		except ValueError:
			console.print("\tPlease enter a valid integer between 1 & 4", style="b red")
		except KeyboardInterrupt:
			console.print("\n")
			pass
		else:
			if choice not in (1, 2, 3, 4):
				console.print("\tPlease enter a valid integer between 1 & 4", style="b red")
				continue
			else:
				break


def startDecryptionProcess():
	StartDecrypt = EnDProcess(message="", key_a="", key_c="")
	inputDSuffix1()
	StartDecrypt.decrypt()
	inputDSuffix2()
	StartDecrypt.writeDecrypted(StartDecrypt.decrypt())


def tableStart():
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("Choice", justify="left")
	table.add_column("Function", justify="left", style="cyan")
	table.add_row("[bold]1[/bold]", "Encrypt a new message into %sdata{{suffix}}.bin." % userfolder)
	table.add_row("[bold]2[/bold]", "Decrypt an encrypted message.")
	table.add_row("[bold]3[/bold]", "Exit Encrypt0")
	table.add_row("[bold]4[/bold]", "View README")
	console.print(table, justify="center")
	console.print("\n")


def main():
	while True:
		try:
			clearScreen()
			sleep(1)
			loadingScreen()
			startScreen()
			tableStart()
			startScreenInput()

			if choice == 1:
				loadingScreen()
				printDir(userfolder)
				startEncryptionProcess()
				sleep(1)

			elif choice == 2:
				loadingScreen()
				printDir(userfolder)
				startDecryptionProcess()
				sleep(1)

			elif choice == 3:
				console.print("Exiting Now", justify="center", style="b red")
				sleep(1)
				clearScreen()
				sys.exit()

			elif choice == 4:
				clearScreen()
				startHelp()
				console.print("\nPress ENTER to continue.", justify="left", style="b cyan", end="")
				input()
		except KeyboardInterrupt:
			pass


if __name__ == '__main__':
	main()
