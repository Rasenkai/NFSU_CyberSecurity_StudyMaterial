import math

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_key_pair(p, q):
    """Generate RSA key pair"""
    # Check if p and q are prime
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both numbers must be prime")

    # Calculate n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi and math.gcd(e, phi) != 1:
        e += 1

    # Return public key (n, e)
    return (n, e)

def encrypt(message, public_key):
    """Encrypt a message using RSA"""
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

if __name__ == '__main__':
    # Get prime numbers from user
    p = int(input('Enter a prime number (p): '))
    q = int(input('Enter another prime number (q): '))

    # Generate public key
    public_key = generate_key_pair(p, q)
    print('Public Key (n, e):', public_key)

    # Get message from user
    message = input('Enter a message to encrypt: ')

    # Encrypt message
    encrypted_message = encrypt(message, public_key)
    print('Encrypted message:', encrypted_message)
