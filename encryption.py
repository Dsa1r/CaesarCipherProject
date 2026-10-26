def encrypt(text, key):
  if not isinstance(key, int) or isinstance(key, bool) or not 0 <= key <= 25:
    raise ValueError("Key must be an integer between 0 and 25.")
  if not isinstance(text, str) or not text.strip():
    raise ValueError("Text cannot be empty.")

result = ""

for char in text:
    if 'A' <= char <= 'Z':
        result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    elif 'a' <= char <= 'z':
        result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    else:
        result += char

return result
