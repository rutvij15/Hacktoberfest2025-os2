# Text Encryption & Decryption Tool (Pure Python - OOP + Algorithms)

class CipherTool:

    def caesar_encrypt(self, text, shift):
        return "".join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper()
                       else chr((ord(c) - 97 + shift) % 26 + 97) if c.islower()
                       else c for c in text)

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)

    def vigenere_encrypt(self, text, key):
        key = key.lower()
        encrypted = []
        key_i = 0
        for c in text:
            if c.isalpha():
                shift = ord(key[key_i % len(key)]) - 97
                encrypted.append(self.caesar_encrypt(c, shift))
                key_i += 1
            else:
                encrypted.append(c)
        return "".join(encrypted)

    def vigenere_decrypt(self, text, key):
        key = key.lower()
        decrypted = []
        key_i = 0
        for c in text:
            if c.isalpha():
                shift = ord(key[key_i % len(key)]) - 97
                decrypted.append(self.caesar_decrypt(c, shift))
                key_i += 1
            else:
                decrypted.append(c)
        return "".join(decrypted)

    def reverse_cipher(self, text):
        return text[::-1]


def main():
    tool = CipherTool()

    while True:
        print("\n=== Encryption Tool ===")
        print("1) Caesar Encrypt")
        print("2) Caesar Decrypt")
        print("3) Vigenere Encrypt")
        print("4) Vigenere Decrypt")
        print("5) Reverse Cipher")
        print("6) Exit")

        choice = input("Choose option: ")

        if choice == "6":
            break

        text = input("Enter text: ")

        if choice in ["1", "2"]:
            shift = int(input("Shift (number): "))
            if choice == "1":
                print("\nEncrypted:", tool.caesar_encrypt(text, shift))
            else:
                print("\nDecrypted:", tool.caesar_decrypt(text, shift))

        elif choice in ["3", "4"]:
            key = input("Enter key (letters only): ")
            if choice == "3":
                print("\nEncrypted:", tool.vigenere_encrypt(text, key))
            else:
                print("\nDecrypted:", tool.vigenere_decrypt(text, key))

        elif choice == "5":
            print("\nResult:", tool.reverse_cipher(text))

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
