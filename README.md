# Encrypto

*-A tool written in Python and implemented in C for quick encryption-*

>Author of Source Code & Documentation: **Aradhya Chakrabarti**

## INTRODUCTION

---
**Encrypt0** is an application created using the `Python(v3.8.6)` programming language. It can quickly encrypt small pieces of alphabetical text for secure transfer. The application itself provides the user options for both encrypting and decrypting data.

---

## INSTALLATION

---
Encrypt0 can be used on devices running on both Windows and GNU/Linux-based operating systems. This application has been tested on `Windows 7(32-bit)` and `Windows 10(64-bit)` operating systems.
It is also possible to run Encrypt0 on GNU/Linux-based devices by directly using the Python interpreter or manually building an executable. (refer to **FURTHER INFORMATION**)

To run **Encrypt0**, on devices running on Windows-based operating systems, open `main.exe`.


---

## USAGE

---
>***IMPORTANT***: In order to make sure that the applications runs without problems make sure that there is a folder called `user` in the same directory as the file `main.exe` on Windows-based devices or generally, the same directory as the executable or `.py` file.

On startup, you see the *Main Dashboard*.


### I. Encryption

Press **1** on the Main Dashboard prompt to encrypt a new message and store into a file. Your message should only include one sentence of any length and only alphabetical characters. (Read *LIMITATIONS* for more information)

You can enter any alphabetical sequence as your *LEVEL1* Key and any integral value between 0 and 26 as your *LEVEL2* Key. (However, use of 0 or 26 is not recommended)

The final prompt during encryption asks for a suffix for your file containing your encrypted data. Here too, only integers (any value) are allowed. Entry of a non integer value will close the program.

>*NOTE*: Encrypt0 neglects the whitespaces inside your message and your LEVEL1 key.

>*WARNING:* This program does not check if a particular suffix has already been used. Use of the same suffix more than once during encryption will corrupt data in the file with that suffix.

Upon successful encryption of your message, you will see the text `MESSAGE SUCCESSFULLY ENCRYPTED TO FILE` on your screen. You should now find a file with a name of the format `data{{suffix}}.bin` in the `user` folder, where `suffix` is the integer you entered earlier as your file suffix.

>*WARNING:* Don't modify this file, since doing so may lead to corruption of your encrypted data.


### II. Decryption


Press **2** if you want to decrypt a file of the format `data{{suffix}}.bin` present in the `user` folder contatining a message initially encrypted by *Encrypt0*.

Here, entry of a non integer in any of the two prompts will close the program.

After successful decryption, you will see the text `MESSAGE SUCCESSFULLY DECRYPTED TO FILE` on your screen. You should now find a file with a name of the format `decrypted{{suffix}}.txt` in the `user` folder, where `suffix` is the integer you entered earlier in the *second* prompt.

>*WARNING:* This program does not check if a particular suffix has already been used. Use of the same suffix more than once during encryption will corrupt data in the file with that suffix.

### III. Exit Encrypt0

Press **3** in the Main Dashboard prompt to exit *Encrypt0*.

### IV. Viewing the README:

Press **4** in the Main Dashboard prompt to view this README again.

---

## LIMITATIONS

---
>1. Although this application can be used to encrypt small messages, this level of encryption is **NOT SECURE** for sensitive data since Encrypt0 only uses a few levels of *Classical Era* ciphers for encryption.

>2. Since Encrypt0 is based on *Classical Era Ciphers*, it does not add any functions to the fundamental working of those ciphers. Therefore, Encrypt0 can only encrypt alphabetical messages.

---

## FURTHER INFORMATION

---
>1. The source code of the whole application is provided in the `source` folder.

>2. To directly run Encrypt0 with Python, ensure your version of Python is >= 3.6.1. Then run `main.py` in the `source` folder with the command:

>>>>\>python main.py
>>>on Windows-based devices.

>>>Or,

>>>>$python3 main.py
>>>on Linux-based devices.

>3. You can also build standalone executables for your system specifically, using the `cython` package.

>>>- To do so, on Windows-based devices, first install `cython` with the command:
>>>>\>python -m pip install cython

>>>Or on Linux-based devices, 
>>>>$python3 -m pip install cython

>>>- Now, we need to create a `.pyx` file. So, just rename `main.py` to `main.pyx` and add the line:
>>>\#cython: language_level=3
>>>to the top of `main.pyx`.

>>>Now, to create the C source code from `main.pyx`, on Windows-based devices,
>>>>\>cython --embed -o \path\to\new\c\file.c \path\to\main.pyx

>>>On Linux-based devices:
>>>>$cython --embed -o /path/to/new/c/file.c /path/to/main.pyx 

>>>This should create a C source code file at the defined path.

>>>- Now, you just need to compile this file into an executable.
>>>You can use `MinGW` on Windows-based devices and `GNU-GCC` on Linux-based devices.
>>>On a Windows-based device with `MinGW` installed and `gcc` already added to `$PATH`, use the command:
>>>>\>gcc -v -Os -I \path\to\python's\include\folder -L \path\to\python\folder  -o \path\to\file.exe \path\to\file.c  -l python??

>>>*Where python?? is just the name of the python dll library without any filetype. For eg: if the dll's name is python38.dll, use 38 in place of ??.*

>>>Similarly on Linux-based devices, the command is same except for the path to the respective libraries.

>>>**This should create an executable file specific to your system architecture for Encrypt0.**

---

## Bibliography

---
>1. Cestari, F. (2017, October 7). PyInstaller ImportError: No module named 'pyfiglet.fonts'. Retrieved January 2021, from [Stack Overflow](https://stackoverflow.com/a/46615852)

>2. Cryptography, P. (n.d.). Autokey Cipher. Retrieved January 2021, from [Practical Cryptography](http://www.practicalcryptography.com/ciphers/autokey-cipher/)

>3. Cryptography, P. (n.d.). Caesar Cipher. Retrieved January 2021, from [Practical Cryptography](http://www.practicalcryptography.com/ciphers/caesar-cipher/)

>4. GeeksForGeeks. (2020, May 10). Autokey Cipher | Symmetric Ciphers. Retrieved January 2021, from [GeeksForGeeks](https://www.geeksforgeeks.org/autokey-cipher-symmetric-ciphers/)

>5. GeeksForGeeks. (2019, August 12). Caesar Cipher in Cryptography. Retrieved January 2021, from [GeeksForGeeks](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)

>6. Matthes, E. (2019). Python Crash Course: A Hands-On, Project-Based Introduction to Programming 2nd edition. No Starch Press.

>7. SuperShoot. (2019, March 31). How to use the try-except command in a while loop asking for user input. Retrieved January 2021, from [Stack Overflow](https://stackoverflow.com/a/55437460)

>8. Sweigart, A. (2018). Cracking Codes with Python An Introduction to Building and Breaking Ciphers. No Starch Press.

---