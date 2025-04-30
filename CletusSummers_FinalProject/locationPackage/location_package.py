# File Name : main.py
# Student Name: Andrew Rozsits, Nate Hoang, Ray Happel, Liam Vasey
# email:  rozsitaj@mail.uc.edu, hoangnd@mail.uc.edu, happelrc@mail.uc.edu, vaseylh@mail.uc.edu
# Assignment Number: Final Assignment
# Due Date:   5/1/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, we are finding a location on campus by decrypting code as well as uploading an image.

# Brief Description of what this module does. This module we are using everything we have learned this semester to decrypt code and find a location. Add packages and modeules, while also importing a txt and jpg file for data to pull from.
# Citations: https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/, https://stackoverflow.com/questions/15474366/adding-an-image-to-a-project-in-visual-studio, chatgpt.com
# Anything else that's relevant:


import json
from cryptography.fernet import Fernet

class Decryptor:
    """
    Decryptor class for handling both index-based location decoding and Fernet message decryption.

    """

    def __init__(self, english_file_path, encrypted_json_path):
        """
        Constructor for the Decryptor class.

        @param english_file_path: Path to the text file containing English words.
        @param encrypted_json_path: Path to the JSON file containing encrypted location indices.
        """
        self.english_file_path = english_file_path
        self.encrypted_json_path = encrypted_json_path
        self.word_list = self._load_english_words()
        self.encrypted_data = self._load_encrypted_data()

    def _load_english_words(self):
        """
        Load English words from the provided text file.

        @return: A list of English words, each line stripped of whitespace.
        """
        with open(self.english_file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]

    def _load_encrypted_data(self):
        """
        Load encrypted team location data from a JSON file.

        @return: A dictionary mapping team names to lists of word indices.
        """
        with open(self.encrypted_json_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def decrypt_location(self, team_name):
        """
        Decrypt the location name for a specific team.

        @param team_name: The name of the team whose location needs to be decrypted.
        @return: A space-separated string representing the location.
        @raises ValueError: If the team is not found in the encrypted data.
        @raises IndexError: If an index in the JSON file is out of bounds of the word list.
        """
        if team_name not in self.encrypted_data:
            raise ValueError(f"Team {team_name} not found.")

        indices = self.encrypted_data[team_name]
        decrypted_words = []

        for index in indices:
            idx = int(index)  # assumes index is already 0-based
            if idx < 0 or idx >= len(self.word_list):
                raise IndexError(f"Index {idx} out of range in UCEnglish.txt.")
            decrypted_words.append(self.word_list[idx])

        return ' '.join(decrypted_words)

    def decrypt_fernet_message(self, key, encrypted_message):
        """
        Decrypt a Fernet-encrypted message.

        @param key: A bytes object containing the Fernet encryption key.
        @param encrypted_message: The encrypted string to be decrypted.
        @return: The decrypted string.
        @raises Exception: If decryption fails.
        """
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_message.encode())
        return decrypted.decode()