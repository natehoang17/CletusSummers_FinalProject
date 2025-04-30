

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

