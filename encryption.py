def validate_key(key):
    return isinstance(key, int) and 0 <= key < 26

def validate_text(text):
    return isinstance(text, str) and len(text) > 0

def encrypt(plaintext, key):
    # Validate inputs
    if not validate_text(plaintext):
        raise ValueError("Text cannot be empty.")
    if not validate_key(key):
        raise ValueError("Key must be between 0 and 25.")

    encrypted_chars = []
    
    for char in plaintext:
        if 'A' <= char <= 'Z':
            # Encrypt uppercase letters
            base = ord('A')
            new_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_chars.append(new_char)
        elif 'a' <= char <= 'z':
            # Encrypt lowercase letters
            base = ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_chars.append(new_char)
        else:
            # Leave spaces and punctuation unchanged
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)