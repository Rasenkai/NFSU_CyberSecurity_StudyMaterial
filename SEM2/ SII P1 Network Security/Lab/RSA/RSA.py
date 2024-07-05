import random
import math

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_key_pair():
    """Generate RSA key pair"""
    # Select two prime numbers
    p = random.randint(2**10, 2**11)
    while not is_prime(p):
        p = random.randint(2**10, 2**11)

    q = random.randint(2**10, 2**11)
    while not is_prime(q):
        q = random.randint(2**10, 2**11)

    # Calculate n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d, the modular multiplicative inverse of e modulo phi
    d = pow(e, -1, phi)

    # Return public and private keys
    return ((n, e), (n, d))

def encrypt(message, public_key):
    """Encrypt a message using RSA"""
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Decrypt an encrypted message using RSA"""
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main program
if __name__ == '__main__':
    # Generate key pair
    public_key, private_key = generate_key_pair()
    print('Public Key (n, e):', public_key)
    print('Private Key (n, d):', private_key)

    # Get message from user
    message = input('Enter a message to encrypt: ')

    # Encrypt message
    encrypted_message = encrypt(message, public_key)
    print('Encrypted message:', encrypted_message)

    # Decrypt message
    decrypted_message = decrypt(encrypted_message, private_key)
    print('Decrypted message:', decrypted_message)
    