def Ascii(Phrase):
    return [ord(char) for char in Phrase]

def format3chiffre(PhraseAscii):
    return [f"{num:03}" for num in PhraseAscii]


def encrypt(NouvelleChaine, e, n):
    ChaineCrypter = [pow(int(x), e, n) for x in NouvelleChaine]
    return ChaineCrypter

def Message(ChaineCrypter):
    return ' '.join(str(x) for x in ChaineCrypter)

def filter_letters(phrase):
    return ''.join(char for char in phrase if char.isalpha())

# Entrée utilisateur
Phrase = input("Enter a phrase: ")
Phrase = filter_letters(Phrase)

if not Phrase:
    print("Error: The input must contain at least one letter (A-Z or a-z).")
else:
    e = int(input("Enter e value: "))
    n = int(input("Enter n value: "))

    # Chiffrement
    PhraseAscii = Ascii(Phrase)
    f3c = format3chiffre(PhraseAscii)
    ChaineCrypter = encrypt(f3c, e, n)
    resultat = Message(ChaineCrypter)
    print("Encrypted Result:", resultat)
