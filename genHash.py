#!/usr/bin/env python3
"""
A simple password hash generator
"""
import crypt
import getpass

#### Functions ####
def getPasswd():
    """
    Function for getting desired password.
    Only returns if passwords match or password isn't too short.
    Otherwise it keeps looping.
    """

    while True:
        userPass1 = getpass.getpass(prompt="Enter your desired password: ")
        if len(userPass1) < 6:
            print("Please use a COUPLE of more characters for your password!")
            continue
        userPass2 = getpass.getpass(prompt="Enter your password again: ")

        if userPass1 != userPass2:
            print("The passwords does not match. Please try again.")
        else:
            return userPass1


def chooseEnc():
    """
    Function for choosing encryption type.
    On incorrect entry, the function keeps looping.
    """

    while True:
        encType = input("Please choose encryption type. \
Enter 'MD5' or 'SHA512': ")

        if encType.upper() not in ['MD5', 'SHA512']:
            print("Incorrect entry.")
        else:
            return encType.upper()
#### End of functions ####

welcome = """
ASHG - A Simple Hash Generator
------------------------------
Enter your desired password twice (for confirmation).
Then choose encryption type.

If you are generating a hash for Rundeck, choose MD5.
If you want to generate a password hash for GNU/Linux,
(/etc/shadow) choose SHA512.

Your hash will be printed to stdout on completion.
--------------------------------------------------
"""

print(welcome)

userPass = getPasswd()
encTypeChoice = chooseEnc()

if encTypeChoice == "MD5":
    userHash = crypt.crypt(userPass, crypt.METHOD_MD5)
elif encTypeChoice == "SHA512":
    userHash = crypt.crypt(userPass, crypt.METHOD_SHA512)

print("Your hash is:")
print(userHash)

exit(0)
