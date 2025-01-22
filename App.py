import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random


# Utility Functions
def Ascii(phrase):
    return [ord(char) for char in phrase]


def format3chiffre(PhraseAscii):
    return [f"{num:03}" for num in PhraseAscii]


def nombre_de_chiffres(n):
    return len(str(n))


def bloc(f3c, n):
    taille_bloc = nombre_de_chiffres(n) - 1
    NouvelleChaine = []
    chaine_complete = ''.join(f3c)

    for i in range(0, len(chaine_complete), taille_bloc):
        bloc = chaine_complete[i:i + taille_bloc]
        if len(bloc) < taille_bloc:
            bloc += '0' * (taille_bloc - len(bloc))
        NouvelleChaine.append(bloc)

    return NouvelleChaine


def encrypt(NouvelleChaine, e, n):
    return [pow(int(x), e, n) for x in NouvelleChaine]


def Message(ChaineCrypter):
    return ' '.join(str(x) for x in ChaineCrypter)


def ReformerBloc(PhraseCrypter, n):
    return PhraseCrypter.split()


def decrypt(ChaineReformer, d, n):
    return [pow(int(x), d, n) for x in ChaineReformer]


def ascii(messageDecrypter):
    return ''.join(chr(int(valeur)) for valeur in messageDecrypter)


def crible(n):
    L = list(range(2, n + 1))
    prem = []
    while len(L) > 0 and (L[0] * L[0]) <= n:
        prem.append(L[0])
        L = [x for x in L if x % L[0] != 0]
    prem.extend(L)
    return prem


def inv_mod(a0, m0):
    a, m, u, s = a0, m0, 1, 0
    while m != 0:
        q, r = divmod(a, m)
        a, m, u, s = m, r, s, u - q * s
    if a == 1:
        while u < 0:
            u += m0
        return u
    else:
        return None


def cles():
    primes = crible(100)
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randint(10, 100)
    while inv_mod(e, m) is None:
        e = random.randint(10, 100)
    d = inv_mod(e, m)
    return e, d, n


# Main Application
def open_encryption_window():
    encryption_window = tk.Toplevel(root)
    encryption_window.title("Cryptage RSA")
    encryption_window.geometry("500x500")
    encryption_window.configure(bg="#222831")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12, "bold"), padding=10)

    frame_keys = ttk.Frame(encryption_window)
    frame_keys.pack(pady=10, padx=20)

    ttk.Label(frame_keys, text="Valeur de e :").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_e = ttk.Entry(frame_keys, width=20)
    entry_e.grid(row=0, column=1, padx=5)

    ttk.Label(frame_keys, text="Valeur de n :").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_n = ttk.Entry(frame_keys, width=20)
    entry_n.grid(row=1, column=1, padx=5)

    def generate_keys():
        e, d, n = cles()
        entry_e.delete(0, tk.END)
        entry_e.insert(0, str(e))
        entry_n.delete(0, tk.END)
        entry_n.insert(0, str(n))

    ttk.Button(frame_keys, text="Générer des clés", command=generate_keys).grid(row=2, column=0, columnspan=2, pady=10)

    frame_message = ttk.Frame(encryption_window)
    frame_message.pack(pady=10, padx=20)

    ttk.Label(frame_message, text="Message à crypter :").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_message = ttk.Entry(frame_message, width=40)
    entry_message.grid(row=0, column=1, padx=5)

    def encrypt_message():
        message = entry_message.get()
        e = int(entry_e.get())
        n = int(entry_n.get())
        ascii_message = Ascii(message)
        formatted_message = format3chiffre(ascii_message)
        blocks = bloc(formatted_message, n)
        encrypted_message = encrypt(blocks, e, n)
        encrypted_message_str = Message(encrypted_message)
        messagebox.showinfo("Message crypté", encrypted_message_str)

    ttk.Button(frame_message, text="Crypter", command=encrypt_message).grid(row=1, column=0, columnspan=2, pady=10)


root = tk.Tk()
root.title("Application de Cryptage RSA")
root.geometry("500x400")
root.configure(bg="#222831")

frame_main = ttk.Frame(root)
frame_main.pack(pady=50)

ttk.Label(frame_main, text="Application de Cryptage RSA", font=("Arial", 16, "bold")).pack(pady=10)

ttk.Button(frame_main, text="Ouvrir la fenêtre de cryptage", command=open_encryption_window).pack(pady=20)

root.mainloop()
