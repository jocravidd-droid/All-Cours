def caesar(text, shift, encrypt=True):  # Cerveau du chiffrage

    if not isinstance(shift, int) or isinstance(shift, bool):
        return "Shift must be an integer value."
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    if not encrypt:
        shift = -shift

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


def encrypt(text, shift):  # Chiffrage ( SOUS-TRAITANT )
    return caesar(text=text, shift=shift)


def decrypt(text, shift):  # Déchiffrage ( SOUS-TRAITANT )
    return caesar(text=text, shift=shift, encrypt=False)


if __name__ == "__main__":
    encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
    decrypted_text = decrypt(encrypted_text, 13)
    print(decrypted_text)
