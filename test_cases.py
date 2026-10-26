import unittest

from encryption import encrypt
from decryption import decrypt
from cryptanalysis import extract_key

class TestCaesarCipher(unittest.TestCase):

    # Encryption tests
    def test_basic_encryption(self):
        self.assertEqual(encrypt("ABC", 3), "DEF")

    def test_wraparound_encryption(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_zero_key_encryption(self):
        self.assertEqual(encrypt("ABC", 0), "ABC")

    def test_case_and_punctuation(self):
        self.assertEqual(
            encrypt("Hello, XYZ!", 3),
            "Khoor, ABC!"
        )

    # Decryption tests
    def test_basic_decryption(self):
        self.assertEqual(decrypt("DEF", 3), "ABC")

    def test_wraparound_decryption(self):
        self.assertEqual(decrypt("ABC", 3), "XYZ")

    def test_preserve_spaces_and_punctuation(self):
        self.assertEqual(
            decrypt("Khoor, ABC!", 3),
            "Hello, XYZ!"
        )

    # Input validation tests
    def test_invalid_encryption_key(self):
        with self.assertRaises(ValueError):
            encrypt("ABC", 26)
      
    def test_negative_decryption_key(self):
        with self.assertRaises(ValueError):
            decrypt("ABC", -1)

    def test_empty_encryption_text(self):
        with self.assertRaises(ValueError):
            encrypt("", 3)

    def test_empty_decryption_text(self):
        with self.assertRaises(ValueError):
            decrypt("", 3)

    # Cryptanalysis tests
    def test_extract_key(self):
        self.assertEqual(extract_key("ABC", "DEF"), 3)

    def test_extract_key_with_wraparound(self):
        self.assertEqual(extract_key("XYZ", "ABC"), 3)

    def test_inconsistent_key(self):
        with self.assertRaises(ValueError):
            extract_key("ABC", "DEG")

    def test_unequal_text_lengths(self):
        with self.assertRaises(ValueError):
            extract_key("ABC", "DE")

    def test_empty_cryptanalysis_input(self):
        with self.assertRaises(ValueError):
            extract_key("", "")

if __name__ == "__main__":
    unittest.main(verbosity=2)
