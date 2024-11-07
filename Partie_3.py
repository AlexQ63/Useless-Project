n1 = int(input("Veuillez rentrer le premier nombre à multiplier : "))
n2 = int(input("Veuillez rentrer le deuxième nombre à multiplier : "))
resultat = n1*n2

reponse = int(input("Quel est le résultat de votre multiplication ? : "))
while reponse != resultat:
    print("Ceci n'est pas la bonne réponse.")
    reponse = int(input("Quel est le résultat de votre multiplication ? : "))

print("Félicitation, c'est bien la bonne réponse")
