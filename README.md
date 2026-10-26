
# Caesar Cipher Project

## Project Overview
This project implements the Caesar Cipher using Python. It demonstrates encryption, decryption, and cryptanalysis through a known-plaintext attack.

## Project Objectives
- Implement Caesar Cipher encryption and decryption.
- Validate user inputs and encryption keys.
- Handle uppercase and lowercase letters, spaces, and punctuation.
- Extract the encryption key using a known-plaintext attack.
- Test the program and verify that all modules work correctly together.

## Team Members and Task Distribution

### Member 1: لطيفة — Team Leader & Encryption
- Implement the encryption function using `C = (P + K) mod 26`.
- Develop the main menu and user interface.
- Handle user input for plaintext and key.
- Integrate all program modules.
- Write Section 1: Introduction.
- Open the presentation and demonstrate encryption.
- Upload the final project to Blackboard.
- Coordinate team meetings and deadlines.

### Member 2: هنا — Decryption & Input Validation
- Implement the decryption function using `P = (C - K) mod 26`.
- Validate the encryption key (0–25).
- Ensure that text input is not empty.
- Handle uppercase and lowercase letters, spaces, and punctuation.
- Write Section 2: Explanation of Caesar Cipher.
- Explain Caesar Cipher and demonstrate decryption.
- Prepare the presentation slides and their design.

### Member 3: حنين — Cryptanalysis
- Implement the known-plaintext attack using `K = (C - P) mod 26`.
- Extract the encryption key from a plaintext–ciphertext pair.
- Handle edge cases, including empty input and non-alphabetic characters.
- Integrate cryptanalysis into the main menu.
- Write Section 3: Cryptanalysis Method.
- Explain and demonstrate the known-plaintext attack.
- Prepare the Reflection Session content.

### Member 4: الرائعة دانا — Testing & Results
- Write and run test cases for encryption, decryption, and cryptanalysis.
- Identify bugs and verify their fixes.
- Confirm that all modules work correctly together.
- Prepare screenshots of sample program executions.
- Write Section 4: Sample Execution Results.
- Prepare Section 5: Source Code and organize the code appendix.
- Present testing results, sample outputs, and edge cases.
- Format the final report using the provided template.

## Project Structure

```text
CaesarCipherProject/
├── main.py
├── encryption.py
├── decryption.py
├── cryptanalysis.py
├── test_cases.py
└── README.md
```

## Encryption and Decryption Formulas

**Encryption:**

`C = (P + K) mod 26`

**Decryption:**

`P = (C - K) mod 26`

**Known-Plaintext Attack:**

`K = (C - P) mod 26`

Where:
- `P` is the plaintext letter's numerical value.
- `C` is the ciphertext letter's numerical value.
- `K` is the encryption key.

## Requirements
- Python 3
- A Python-compatible code editor or IDE

No external libraries are required if the project uses only Python's standard library.

## How to Run

Run the main program:

```bash
python main.py
```

Run the test cases:

```bash
python test_cases.py
```

## Example

**Encryption**

```text
Plaintext: ABC
Key: 3
Ciphertext: DEF
```

**Decryption**

```text
Ciphertext: DEF
Key: 3
Plaintext: ABC
```

**Cryptanalysis**

```text
Plaintext: ABC
Ciphertext: DEF
Extracted Key: 3
```

## Testing
The program should be tested with:
- Valid and invalid keys.
- Empty text input.
- Letters near the end of the alphabet.
- Uppercase and lowercase letters.
- Spaces and punctuation.
- Integration of all modules.

Actual test results should be recorded in the final report.

## Limitations
The Caesar Cipher is a classical educational cipher and is not suitable for protecting sensitive information because it has a small key space and is vulnerable to brute-force attacks.

## Conclusion
This project provides practical experience in classical encryption, decryption, cryptanalysis, Python modular programming, input validation, and software testing.
