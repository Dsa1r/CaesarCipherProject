def show_menu():
    print("\n==============================")
    print("          CAESAR CIPHER TOOL")
    print("==============================")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Known plaintext attack")
    print("4. Exit")
    print("==============================")

def read_key():
    # keep asking until the user gives a valid key
    while True:
        value = input("Enter key (0-25): ")

        # make sure the input is a number
        try:
            key = int(value)
        except ValueError:
            print("Key must be a number, try again.")
            continue

        # make sure the number is between 0 and 25
        if not validate_key(key):
            print("Key must be between 0 and 25, try again.")
            continue
        return key

def read_text(message):
    # keep asking until the user gives non empty text
    while True:
        text = input(message)

        if not validate_text(text):
            print("Text cannot be empty, try again.")
            continue
        return text

def do_encrypt():
    print("\n--- Encryption ---")
    text = read_text("Enter plaintext: ")
    key = read_key()

    try:
        cipher = encrypt(text, key)
    except ValueError as e:
        print("Error:", e)
        return

    print("Plaintext  :", text)
    print("Key        :", key)
    print("Ciphertext :", cipher)

def do_decrypt():
    print("\n--- Decryption ---")
    text = read_text("Enter ciphertext: ")
    key = read_key()

    try:
        plain = decrypt(text, key)
    except ValueError as e:
        print("Error:", e)
        return

    print("Ciphertext :", text)
    print("Key        :", key)
    print("Plaintext  :", plain)

def do_attack():
    print("\n--- Known Plaintext Attack ---")
    plain = read_text("Enter known plaintext: ")
    cipher = read_text("Enter the ciphertext: ")

    try:
        key = known_plaintext_attack(plain, cipher)
    except ValueError as e:
        print("Error:", e)
        return
    print("Recovered key:", key)

def main():
    print("Welcome to the Caesar Cipher Tool")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            do_encrypt()
        elif choice == "2":
            do_decrypt()
        elif choice == "3":
            do_attack()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Wrong choice, please enter 1, 2, 3 or 4.")

main()
