# encryption 
# formula: C = (P + K) mod 26 

 
def encrypt(text, key): 
  
    # validate inputs first 
    if not validate_key(key): 
        raise ValueError("Key must be an integer between 0 and 25.") 

    if not validate_text(text): 
        raise ValueError("Text cannot be empty.") 

    result = "" 

    for ch in text: 
        if ch.isalpha() and ch.isascii(): 
            # uppercase letters start from A, lowercase from a 

            if ch.isupper(): 
                base = ord('A') 

            else: 
                base = ord('a') 

            # apply the caesar formula 
            new_pos = (ord(ch) - base + key) % 26 
            result = result + chr(base + new_pos) 

        else: 
            # spaces, numbers and punctuation stay the same 
            result = result + ch 

    return result
