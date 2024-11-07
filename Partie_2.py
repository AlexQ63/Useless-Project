from unidecode import unidecode

def rot_13(text):
    text = input("Veuillez rentrer le texte à chiffrer : ")
    key = 13
    k = ""
    for lettre in text:
        lettre = unidecode(lettre)
        if lettre.isalpha():
            chiffrement = chr(ord(lettre) + key)
            if chiffrement.isalpha() is False:
                chiffrement = chr(ord(chiffrement) - 26)
            k += chiffrement
    return k

text = ""
print(rot_13(text))