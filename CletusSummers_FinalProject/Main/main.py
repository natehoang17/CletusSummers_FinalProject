# File Name : main.py
# Student Name: Andrew Rozsits, Nate Hoang, Raymond Happel, Liam Vasey
# email:  rozsitaj@mail.uc.edu, hoangnd@mail.uc.edu, happelrc@mail.uc.edu, vaseylh@mail.uc.edu
# Assignment Number: Final Assignment
# Due Date:   5/1/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, we are finding a location on campus by decrypting code as well as uploading an image.

# Brief Description of what this module does. This module we are using everything we have learned this semester to decrypt code and find a location. Add packages and modeules, while also importing a txt and jpg file for data to pull from.
# Citations: chatgpt.com
# Anything else that's relevant:


import sys
import os
import webbrowser
import json
from cryptography.fernet import Fernet
from locationPackage.location_package import Decryptor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def decrypt_fernet_message(key, encrypted_message):
    """
    Decrypt a Fernet-encrypted message using the provided key.

    @param key: The Fernet key used for decryption.
    @param encrypted_message: The encrypted message string.
    @return: The decrypted message as a UTF-8 string.
    @raises Exception: If decryption fails due to an invalid key or corrupted data.
    """
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message.encode())
    return decrypted.decode()

def main():
    """
    Main execution function.

    @raises Exception: If file loading or decryption operations fail.
    """
    english_file = 'data/UCEnglish.txt'
    group_hints_file = 'data/EncryptedGroupHints Spring 2025.json'
    team_messages_file = 'data/TeamsAndEncryptedMessagesForDistribution.json'

    team_name = "Cletus Summers"

