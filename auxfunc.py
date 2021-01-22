import subprocess
import platform
import pyfiglet
import time
import os
import sys

"""
    Author of Source Code:
                Aradhya Chakrabarti

"""

width = os.get_terminal_size().columns


def clearScreen():
	""" Function to clear terminal screen """
	if platform.system() == "Windows":
		subprocess.Popen("cls", shell=True).communicate()
	else:  # Linux and Mac
		print("\033c", end="")


def pyfiglet_icon():
	""" Function to use pyfiglet library to create ASCII logo """
	result = pyfiglet.figlet_format("Encrypt0", font="bulbhead")
	print(result)


def sleep_global():
	""" Function to stop execution using time module """
	time.sleep(1)


def loadingScreen():
	""" Function to create loading screen animation """
	clearScreen()
	print("Loading:")
	animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
				"[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
				"[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"
				]
	for i in range(len(animation)):
		time.sleep(0.2)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()
	print("\n")
	clearScreen()


if __name__ == '__main__':
	# main()
	pass
