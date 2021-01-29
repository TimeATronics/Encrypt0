import subprocess
import platform
import pyfiglet
import time
import os
import sys
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown


console = Console()
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
# Name:        auxfunc
# Purpose:     Python module containing auxiliary function definitions
#
# Author:      Aradhya Chakrabarti
#
# Created:     18/01/2021
# Copyright:   (c) Aradhya Chakrabarti 2021
# Licence:     GNU General Public License v3.0
# -------------------------------------------------------------------------------


def clearScreen():
    """ Function to clear terminal screen """
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")


def printDir(dir):
    try:
        if os.path.isdir('./user/'):
            print("\n\tThe %s Directory contains:\n" % dir)
            for root, dirs, files in os.walk(dir):
                level = root.replace(dir, '').count(os.sep)
                indent = '| ' * level
                print('\t\t{}{} \\\n'.format(indent, os.path.basename(root)))
                subindent = '| ' * (level + 1)
                for f in files:
                    print('\t\t{}{}\n'.format(subindent, f))
        else:
            console.print("\tFile and/or directory not found.", style="b red")
            console.print("\n\tTry again next time.", style="b red")
            console.print("Exiting Now", justify="center", style="b red")
            time.sleep(3)
            clearScreen()
            sys.exit()

    except FileNotFoundError:
        console.print("\tFile and/or directory not found.", style="b red")
        console.print("\n\tTry again next time.", style="b red")
        console.print("Exiting Now", justify="center", style="b red")
        time.sleep(3)
        clearScreen()
        sys.exit()
    except KeyboardInterrupt:
        console.print("\n")
        pass


def pyfiglet_icon():
    """ Function to use pyfiglet library to create ASCII logo """
    result = pyfiglet.figlet_format("Encrypt0", font="bulbhead", justify="center")
    return result


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


def inputMessage():
    """Function for taking input of message to be encrypted"""
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
    # To remove all other elements in input than alphabets.
    list1 = [i for i in message if i in input_dict_c.keys()]
    sep = ""
    message = sep.join(list1)
    length = len(message)


def inputKeyA():
    """ Function for taking input of KEY_LEVEL1 """
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
    # To remove all other elements in key_a than alphabets.
    list2 = [i for i in key_a if i in input_dict_a.keys()]
    sep = ""
    key_a = sep.join(list2)


def inputKeyC():
    """ Function for taking input of KEY_LEVEL2 """
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


def keyCGlobal():
    """ Function for making key_c available to main.py """
    return key_c


def inputSuffix():
    """ Function to input suffix for data{{suffix}}.bin (foor encryption) """
    # This is a normal returnable function called inside writeEncrypted()

    try:
        console.print("\n\tEnter an integer suffix for \
new filename\n\t[bold red]>>> [/bold red]", style="b green", end="")
        suffix = int(input())
    except ValueError:
        console.print("\tPlease enter an integer value", style="b red")
        console.print("\n\tTry again next time.", style="b red")
        console.print("Exiting Now", justify="center", style="b red")
        time.sleep(3)
        clearScreen()
        sys.exit()
    except KeyboardInterrupt:
        console.print("\n")
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
        console.print("\n\tEnter desired integer suffix for \
data{{suffix}}.bin\n\t[bold red]>>> [/bold red]", style="b green", end="")
        dsuffix1 = int(input())
    except ValueError:
        console.print("\tPlease enter an integer value", style="b red")
        console.print("\n\tTry again next time.", style="b red")
        console.print("Exiting Now", justify="center", style="b red")
        time.sleep(3)
        clearScreen()
        sys.exit()
    except KeyboardInterrupt:
        console.print("\n")
        pass


def inputDSuffix2():
    """ Function to input suffix for decrypted{{suffix}}.txt """
    # This variable is global since decrypt function is called in writeDecrypted
    # Hence is this function is calles in writeDecrypted,
    # Loop of calls would be made.

    global dsuffix2

    try:
        console.print("\n\tEnter an integer suffix for new \
file (decrypted{{suffix}}.txt)\n\t[bold red]>>> [/bold red]", style="b green", end="")
        dsuffix2 = int(input())
    except ValueError:
        console.print("\tPlease enter an integer value", style="b red")
        console.print("\n\tTry again next time.", style="b red")
        console.print("Exiting Now", style="b red", justify="center")
        time.sleep(3)
        clearScreen()
        sys.exit()
    except KeyboardInterrupt:
        console.print("\n")
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

        encrypted_c = caesarEncrypt(message, key_c)
        key_new = full_key(message, key_a)
        encrypted_a = autokeyEncrypt(encrypted_c, key_new)

        return encrypted_c, encrypted_a, key_new

    def writeEncrypted(self, encrypted_a, key_new, key_c):
        """ Function to write encrypted message + "#@" ... to data{{suffix}}.bin """

        suffix = inputSuffix()
        data_filename = f'data{suffix}.bin'

        try:
            file = open('./user/%s' % data_filename, "wb+")
        except FileNotFoundError:
            console.print("\tFile and/or directory not found.", style="b red")
            console.print("\n\tTry again next time.", style="b red")
            console.print("Exiting Now", justify="center", style="b red")
            time.sleep(3)
            clearScreen()
            sys.exit()
        except KeyboardInterrupt:
            console.print("\n")
            pass

        writedata = str(encrypted_a + "#@" + key_new + "#@" + str(key_c))

        writebinary = strtobin(writedata)  # convert writedata to binary "string"

        file.write(writebinary.encode("utf-8"))  # write binary "string" as utf-8
        file.close()

        console.print("MESSAGE SUCCESSFULLY ENCRYPTED TO FILE", justify="center", style="b magenta")
        time.sleep(2)

    def decrypt(self):
        """ Function to read and decrypt data from ~.data after splitting terms """

        global decrypted

        data_filename = f'data{dsuffix1}.bin'

        try:
            file = open('./user/%s' % data_filename, "rb")
        except FileNotFoundError:
            console.print("\tFile and/or directory not found.", style="b red")
            console.print("\n\tTry again next time.", style="b red")
            console.print("Exiting Now", justify="center", style="b red")
            time.sleep(3)
            clearScreen()
            sys.exit()
        except KeyboardInterrupt:
            console.print("\n")
            pass

        data = file.read()
        data_decode = bintostr(data)  # convert "data" to ascii mapping
        file.close()

        list_data = data_decode.split("#@")  # splitting the string w.r.t #@
        encrypted_a = list_data[0]
        key_new = list_data[1]
        key_c = int(list_data[2])

        decrypted_c = autokeyDecrypt(encrypted_a, key_new)
        decrypted = caesarDecrypt(decrypted_c, key_c)
        return decrypted

    def writeDecrypted(self, decrypted):
        """ Function to write decrypted text to decrypted.txt """

        decrypted_filename = f'decrypted{dsuffix2}.txt'

        try:
            file = open('./user/%s' % decrypted_filename, "wb+")
        except Exception:
            pass
        except KeyboardInterrupt:
            console.print("\n")
            pass
        else:
            if os.path.isdir('./user/'):
                pass
            else:
                console.print("\tFile and/or directory not found.", style="b red")
                console.print("\n\tTry again next time.", style="b red")
                console.print("Exiting Now", justify="center", style="b red")
                time.sleep(3)
                clearScreen()
                sys.exit()

        file = open('./user/%s' % decrypted_filename, "w")
        file.write(decrypted)
        file.close()
        console.print("MESSAGE SUCCESSFULLY DECRYPTED TO FILE", justify="center", style="b magenta")
        time.sleep(2)


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
    icon = pyfiglet_icon()
    console.print(icon, style="red b")
    console.print("\nHello and welcome to ENCRYPT0", justify="center", style="b cyan")
    console.print("This is a program written in Python to help \n\
you encrypt small alphabetical messages.\n", justify="center", style="b green")


def startHelp():
    """ Function to display same help text """
    try:
        readme = open("README.md", encoding="utf-8")
        markdown = Markdown(readme.read())
        console.print(markdown)
    except FileNotFoundError:
        console.print("\tFile and/or directory not found.", style="b red")
        console.print("\n\tTry again next time.", style="b red")
        console.print("Exiting Now", justify="center", style="b red")
        time.sleep(3)
        clearScreen()
        sys.exit()
    except KeyboardInterrupt:
        console.print("\n")
        pass


def startScreenInput():
    """ Function to take input in main window """
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
    """ Function to create instance of EnDProcess and call decrypt function """
    StartDecrypt = EnDProcess(message="", key_a="", key_c="")
    inputDSuffix1()
    StartDecrypt.decrypt()
    inputDSuffix2()
    StartDecrypt.writeDecrypted(StartDecrypt.decrypt())


def tableStart():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Choice", justify="left")
    table.add_column("Function", justify="left", style="cyan")
    table.add_row("[bold]1[/bold]", "Encrypt a new message into ./user/data{{suffix}}.bin.")
    table.add_row("[bold]2[/bold]", "Decrypt an encrypted message.")
    table.add_row("[bold]3[/bold]", "Exit Encrypt0")
    table.add_row("[bold]4[/bold]", "View README")

    console.print(table, justify="center")
    console.print("\n")


def main():
    """ Main function which is executed """
    # This loop is to enable user input after any one process and not abruptly exit.
    while True:
        try:
            startSequence()
            startScreen()
            tableStart()
            startScreenInput()

            if choice == 1:
                loadingScreen()
                printDir("./user")
                startEncryptionProcess()
                time.sleep(1)

            elif choice == 2:
                loadingScreen()
                printDir("./user")
                startDecryptionProcess()
                time.sleep(1)

            elif choice == 3:
                console.print("Exiting Now", justify="center", style="b red")
                sleep_global()
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
