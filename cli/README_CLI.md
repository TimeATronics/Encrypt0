# Encrypt0-CLI

*-Command Line Implementation of Encrypt0-*

>Author of Source Code & Documentation: **Aradhya Chakrabarti**

## INTRODUCTION

---
**Encrypt0-CLI** is an application created using the `Python(v3.8.6)` programming language. It can quickly encrypt small pieces of alphabetical text for secure transfer. The application itself provides the user options for both encrypting and decrypting data through the command line itself.

---

## INSTALLATION

---
Encrypt0-CLI can be used on devices running on both Windows and GNU/Linux-based operating systems. This application has been tested on `Windows 7(32-bit)` and `Windows 10(64-bit)` operating systems.
It is also possible to run Encrypt0 on GNU/Linux-based devices by directly using the Python interpreter or manually building an executable. (refer to **FURTHER INFORMATION**)

To run **Encrypt0-CLI**, on devices running on Windows-based operating systems, follow the instructions under **USAGE**.

---

## USAGE

### I. Encryption

---
In a command line window, type:
>\>\path\to\encrypt.exe -file \path\to\new\file -text {the message you want to encrypt) -key1 {your LEVEL1 KEY} -key2 {your LEVEL2 KEY}
>
>(Usage of {} is to show position of arguments.)
>
>*Example Usage:*
>\>.\encrypt.exe -file .\message1 -text Hello World -key1 Key One -key2 15

>**NOTE:** All arguments (-file, -text, etc. given above are compulsory for execution of the program.)
>You can optionally use the single argument "-h" or "--help" to read more instructions about usage of the program.

Your message should only include one sentence of any length and only alphabetical characters. (Read *LIMITATIONS* for more information)

You can enter any alphabetical sequence as your *LEVEL1* Key and any integral value between 0 and 26 as your *LEVEL2* Key. (However, use of 0 or 26 is not recommended)

>*NOTE*: Encrypt0-CLI neglects the whitespaces inside your message and your LEVEL1 key.

>*WARNING:* This program does not check if a particular suffix has already been used. Use of the same suffix more than once during encryption will corrupt data in the file with that suffix.

Upon successful encryption of your message, you will see the text `MESSAGE SUCCESSFULLY ENCRYPTED TO FILE` on your screen. You should now find a file with the name you specified in the specified folder.

>*WARNING:* Don't modify this file, since doing so may lead to corruption of your encrypted data.

---

### II. Decryption

---
To decrypt a message stored in a file encrypted using Encrypt0, type:
>\>\path\to\decrypt.exe -file \path\to\encrypted\file

>*Example Usage:*
>\>.\decrypt.exe -file .\message1

After successful decryption, you should see a message of the format:
>Decrypted message from the file "{your file name}" is:
>       {YOUR DECRYPTED MESSAGE}

>*WARNING:* This program does not check if a particular suffix has already been used. Use of the same suffix more than once during encryption will corrupt data in the file with that suffix.

---

## LIMITATIONS

---
>1. Although this application can be used to encrypt small messages, this level of encryption is **NOT SECURE** for sensitive data since Encrypt0 only uses a few levels of *Classical Era* ciphers for encryption.

>2. Since Encrypt0 is based on *Classical Era Ciphers*, it does not add any functions to the fundamental working of those ciphers. Therefore, Encrypt0 can only encrypt alphabetical messages.

---

## FURTHER INFORMATION

---
>1. The source code of the whole application is provided in the `source` folder.

>2. To directly run Encrypt0-CLI with Python, ensure your version of Python is >= 3.6.1. Then run the desired `.py` in the `source` folder with the command:

>>\>python {}.py
>
>>({} represents either "encrypt" or "decrypt")
>>on Windows-based devices.

>>Or,

>>$python3 {}.py
>>on Linux-based devices.

>3. You can also build standalone executables for your system specifically, using the `cython` package.
>>*(Refer to the "FURTHER INFORMATION" section in the README for the TUI implementation of Encrypt0 for
>>more information. Steps followed are similar.)*

---

## License

---
Encrypt0 is free software licensed under the General Public License, version 3.0.
Please see the license headers at the tops of individual source files.

___
