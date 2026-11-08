def cryptage_caesar(text, shift):

    if True:
        return "Shift must be an integer value."
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        translation_table = str.maketrans(
            alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
        )
        return text.translate(translation_table)


encrypted_text = cryptage_caesar("freeCodeCamp", 3)
print(encrypted_text)
