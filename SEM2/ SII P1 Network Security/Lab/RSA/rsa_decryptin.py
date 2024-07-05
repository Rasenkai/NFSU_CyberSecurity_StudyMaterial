def decrypt(encrypted_message, private_key):
    """Decrypt an encrypted message using RSA"""
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

if __name__ == '__main__':
    # Get private key from user
    n = int(input('Enter the value of n: '))
    d = int(input('Enter the value of d: '))
    private_key = (n, d)

    # Get encrypted message from user
    encrypted_message = input('Enter the encrypted message (space-separated values): ')
    encrypted_message = [int(char) for char in encrypted_message.split()]

    # Decrypt message
    decrypted_message = decrypt(encrypted_message, private_key)
    print('Decrypted message:', decrypted_message)
