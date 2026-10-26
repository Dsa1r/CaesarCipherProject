from encryption import encrypt
from decryption import decrypt
from cryptanalysis import extract_key

def main():
    while True:
        print("\n=== Caesar Cipher ===")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Cryptanalysis")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        try:

            if choice == "1":
                text = input("Enter plaintext: ")
                key = int(input("Enter key (0-25): "))
              
                result = encrypt(text, key)
                print("Ciphertext:", result)

            elif choice == "2":
                text = input("Enter ciphertext: ")
                key = int(input("Enter key (0-25): "))
              
                result = decrypt(text, key)
                print("Plaintext:", result)

            elif choice == "3":
                plaintext = input("Enter known plaintext: ")
                ciphertext = input("Enter corresponding ciphertext: ")

                key = extract_key(plaintext, ciphertext)
                print("Extracted key:", key)

            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
