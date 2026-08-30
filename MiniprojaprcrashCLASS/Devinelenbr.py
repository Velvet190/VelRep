import random
import time

print("""
Bonjour !
Le programme choisit un chiffre entre 1 et 100, a toi de le deviner !
Bonne chance !""")
input("(Appuyez sur Entrée pour continuer...)")
print("\n")

a = 0
essai = 1
gagne = False

while True:
    try:
        print("""
1 - Difficulté Facile (1 - 50)
2 - Difficulté Moyen (1 - 100)
3 - Difficulté Difficile (1 - 500)\n"""
        )
        a = int(input("Choisis la difficulté : "))
        if a > 3 or a < 1:
            print("Choisissez uniquement entre 1, 2 et 3 !")
        elif a == 1:
            rep = random.randint(1, 50)
            tentative = 10
            break
        elif a == 2:
            rep = random.randint(1, 100)
            tentative = 7
            break
        elif a == 3:
            rep = random.randint(1, 500)
            tentative = 3
            break
    except ValueError:
        print("Veuillez entrer une valeur valide !")

while tentative != 0:
    try:
        a = int(input("Ta proposition : "))
        if a > rep:
            print("La valeur est plus petite !")
            tentative -= 1
            essai += 1
            print("Il te reste", tentative, "tentative(s)")
        elif a < rep:
            print("La valeur est plus grande !")
            tentative -= 1
            essai += 1
            print("Il te reste", tentative, "tentative(s)")
        elif a == rep:
            print("Bravo tu as trouvé la valeur qui était : ", rep)
            print("\nTu as trouvé au bout de", essai, "essais !")
            gagne = True
            break
    except ValueError:
        print("Veuillez entrer une valeur valide !")
if not gagne:
    time.sleep(0.5)
    print("\nTu as perdu !!\n")
    print("Le nombre etait", rep)
