def validate_key(key):
    return isinstance(key, int) and 0 <= key < 26

def validate_text(text):
    return isinstance(text, str) and len(text) > 0

def decrypt(ciphertext, key):
    # Validate inputs
    if not validate_text(ciphertext):
        raise ValueError("Text cannot be empty.")
    if not validate_key(key):
        raise ValueError("Key must be between 0 and 25.")

    decrypted_chars = []
    
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            # Decrypt uppercase letters
            base = ord('A')
            new_char = chr((ord(char) - base - key) % 26 + base)
            decrypted_chars.append(new_char)
        elif 'a' <= char <= 'z':
            # Decrypt lowercase letters
            base = ord('a')
            new_char = chr((ord(char) - base - key) % 26 + base)
            decrypted_chars.append(new_char)
        else:
            # Leave spaces and punctuation unchanged
            decrypted_chars.append(char)
            
    return "".join(decrypted_chars)