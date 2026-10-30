def validate_key(key):
"""
    Validates the shift key.
    Ensures the key is an integer and strictly between 0 and 25.
    """
    if not isinstance(key, int) or isinstance(key, bool) or not 0 <= key <= 25:
        raise ValueError("Key must be an integer between 0 and 25.")

def validate_text(text):
    """
    Validates the text input.
    Ensures the input is a valid string and not empty or whitespace-only.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text cannot be empty.")

def decrypt(text, key):
    """
    Decrypts the given ciphertext using the Caesar Cipher formula: P = (C - K) mod 26.
    Preserves uppercase, lowercase, spaces, and punctuation.
    """
    # Validate inputs before processing decryption
    validate_key(key)
    validate_text(text)
  
    result = ""
# Iterate through each character in the ciphertext
    for char in text:
        # Decrypt uppercase letters (ASCII 65-90)
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            # Decrypt lowercase letters (ASCII 97-122)
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            # Leave spaces, numbers, and punctuation untouched
        else:
            result += char

    return result
