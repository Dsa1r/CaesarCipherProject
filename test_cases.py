import unittest

class TestCaesarCipher(unittest.TestCase):
    # Regular encryption tests
    
    def test_basic_encryption(self):
        # Let's test basic encryption with a normal shift to make sure things work
        self.assertEqual(encrypt("ABC", 3), "DEF")

    def test_wraparound_encryption(self):
        # Make sure letters wrap around correctly if they go past Z (so Z becomes A)
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_zero_key_encryption(self):
        # If the key is zero, the text should stay completely untouched
        self.assertEqual(encrypt("ABC", 0), "ABC")

    def test_case_and_punctuation(self):
        # Make sure uppercase/lowercase, spaces, and symbols are all preserved
        self.assertEqual(
            encrypt("Hello, XYZ!", 3),
            "Khoor, ABC!"
        )

    # Decryption tests
    
    def test_basic_decryption(self):
        # Standard decryption test to make sure it brings the text back to normal
        self.assertEqual(decrypt("DEF", 3), "ABC")

    def test_wraparound_decryption(self):
        # Decryption test with backward alphabet wraparound
        self.assertEqual(decrypt("ABC", 3), "XYZ")

    def test_preserve_spaces_and_punctuation(self):
        # Check that spaces and symbols remain intact after decryption
        self.assertEqual(
            decrypt("Khoor, ABC!", 3),
            "Hello, XYZ!"
        )

    # Input validation tests
    
    def test_invalid_encryption_key(self):
        # Keys of 26 or more should be rejected with a ValueError
        with self.assertRaises(ValueError):
            encrypt("ABC", 26)
        
    def test_negative_decryption_key(self):
        # Negative keys are not allowed
        with self.assertRaises(ValueError):
            decrypt("ABC", -1)

    def test_empty_encryption_text(self):
        # If text is empty during encryption, it must throw an error
        with self.assertRaises(ValueError):
            encrypt("", 3)

    def test_empty_decryption_text(self):
        # Same thing if text is empty during decryption
        with self.assertRaises(ValueError):
            decrypt("", 3)

    # Cryptanalysis tests (Known Plaintext Attack)
    
    def test_known_plaintext_attack(self):
        # Let's see if we can grab the right key using a known plaintext and its ciphertext
        self.assertEqual(known_plaintext_attack("ABC", "DEF"), 3)

    def test_known_plaintext_attack_with_wraparound(self):
        # Key extraction with character wraparound
        self.assertEqual(known_plaintext_attack("XYZ", "ABC"), 3)

    def test_inconsistent_key(self):
        # If the letters have mismatched shifts (not a single valid key), reject it
        with self.assertRaises(ValueError):
            known_plaintext_attack("ABC", "DEG")

    def test_unequal_text_lengths(self):
        # Plaintext and ciphertext lengths have to be equal
        with self.assertRaises(ValueError):
            known_plaintext_attack("ABC", "DE")

    def test_empty_cryptanalysis_input(self):
        # If inputs are empty, it should fail and raise a ValueError
        with self.assertRaises(ValueError):
            known_plaintext_attack("", "")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
