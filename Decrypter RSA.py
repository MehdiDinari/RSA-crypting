
def decrypt(ChaineCrypter, d, n):
    ChaineDecrypter = [pow(x, d, n) for x in ChaineCrypter]
    return ChaineDecrypter

def reformat_to_ascii(DecryptedList):
    return [chr(int(num)) for num in DecryptedList]

# Entrée utilisateur
resultat = input("Enter the encrypted message: ")
d = int(input("Enter d value (private key): "))
n = int(input("Enter n value: "))

# Déchiffrement
try:
    ChaineCrypter = list(map(int, resultat.split()))
    DecryptedAscii = decrypt(ChaineCrypter, d, n)
    OriginalMessage = reformat_to_ascii(DecryptedAscii)
    print("Decrypted Result:", ''.join(OriginalMessage))
except ValueError:
    print("Error: Invalid input format.")
