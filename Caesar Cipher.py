def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            stay_in_alphabet = 65 if char.isupper() else 97
            result += chr((ord(char) - stay_in_alphabet + shift) % 26 + stay_in_alphabet)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Take input from the user
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g. 3): "))
choice = input("Do you want to Encrypt or Decrypt? (E/D): ").upper()

if choice == 'E':
    encrypted = encrypt(message, shift_value)
    print("Encrypted message:", encrypted)
elif choice == 'D':
    decrypted = decrypt(message, shift_value)
    print("Decrypted message:", decrypted)
else:
    print("Invalid choice. Please enter E or D.")