def mod_exp(base, exponent, modulus):
    """Calculate modular exponentiation"""
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

def diffie_hellman():
    """Perform Diffie-Hellman key exchange"""
    # Get prime number and base from user
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g): "))

    # Get private key of user 1
    private_key1 = int(input("User 1: Enter your private key: "))

    # Compute public key of user 1
    public_key1 = mod_exp(g, private_key1, p)

    # Get private key of user 2
    private_key2 = int(input("User 2: Enter your private key: "))

    # Compute public key of user 2
    public_key2 = mod_exp(g, private_key2, p)

    # Exchange public keys
    print("\n--- Public Key Exchange ---")
    print("User 1 sends public key:", public_key1)
    print("User 2 sends public key:", public_key2)
    print("---------------------------")

    # Compute shared secret key
    secret_key1 = mod_exp(public_key2, private_key1, p)
    secret_key2 = mod_exp(public_key1, private_key2, p)

    # Check if both secret keys are equal
    if secret_key1 == secret_key2:
        print("\n--- Shared Secret Key ---")
        print("Shared secret key:", secret_key1)
        print("------------------------")
    else:
        print("Error: Shared secret keys do not match!")

# Main program
if __name__ == '__main__':
    diffie_hellman()
