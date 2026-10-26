def extract_key(plaintext, ciphertext):
    if not isinstance(plaintext, str) or not isinstance(ciphertext, str):
        raise ValueError("Inputs must be strings.")

    if not plaintext.strip() or not ciphertext.strip():
        raise ValueError("Inputs cannot be empty.")

    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext and ciphertext must have equal lengths.")

    extracted_key = None
    matched_letters = 0

    for p_char, c_char in zip(plaintext, ciphertext):
        p_is_letter = (
            'A' <= p_char <= 'Z' or 'a' <= p_char <= 'z'
        )
        c_is_letter = (
            'A' <= c_char <= 'Z' or 'a' <= c_char <= 'z'
        )

        if p_is_letter != c_is_letter:
            raise ValueError(
                "Plaintext and ciphertext must align at each position."
            )

        if not p_is_letter:
            if p_char != c_char:
                raise ValueError(
                    "Non-alphabetic characters must match."
                )
            continue

        p_value = ord(p_char.upper()) - ord('A')
        c_value = ord(c_char.upper()) - ord('A')
        key = (c_value - p_value) % 26
        matched_letters += 1
      
        if extracted_key is None:
            extracted_key = key
        elif key != extracted_key:
            raise ValueError(
                "The letter pairs do not match a single Caesar key."
            )

    if matched_letters == 0:
        raise ValueError("At least one matching letter pair is required.")

    return extracted_key
