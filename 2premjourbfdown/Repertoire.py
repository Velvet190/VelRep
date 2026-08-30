import time

notes = {
    "Alice": 15,
    "Bob": 8,
    "Charlie": 17,
    "David": 11
}
choix = 0

print("""
Bonjour !
Bienvenue dans l'application de gestions de notes de vos élèves, ici vous pourrez modifier les notes des élèves, ajouter des élèves si nécessaire et voir les notees actuelles de chaque élèves !
Pour sélectionner ce que vous voulez faire, servez-vous de 1, 2, 3 et 4 pour naviguer dans les menus !
Bonne utilisation !""")
input("(Appuyez sur Entrée pour continuer...)")
print("\n")

def afficher_notes():
    for nom, note in notes.items():
        print(nom, note)
    time.sleep(1)
    print("\n")

while choix != 4:

    print("1. Afficher les notes")
    print("2. Ajouter un élève")
    print("3. Modifier une note")
    print("4. Quitter\n")

    try:
        choix = int(input("Votre choix : "))
        print("\n")

        if choix > 4 or choix <= 0:
            print("Veuillez choisir un chiffre entre 1, 2, 3 et 4 !\n")
            time.sleep(2)
        elif choix == 1:
            afficher_notes()
        elif choix == 2:
                name = input("Nom de l'élève : ")
                time.sleep(1)
                while True:
                    try:
                        note = int(input(f"Note de {name} : "))
                        if 0 <= note <= 20:
                            time.sleep(1)
                            break
                        print("Erreur, la note doit être comprise entre 0 et 20.")
                        time.sleep(1)
                    except ValueError:
                        print("Erreur, veuillez entrer un nombre entier valide !")
                notes.update({name : note})
                time.sleep(1)
                print("\nNotes mises à jour !\n")
                time.sleep(1)
        elif choix == 3:
            name = str(input("Nom EXACT de l'élève : "))
            time.sleep(1)
            if name in notes:
                while True:
                    try:
                        note = int(input(f"Nouvelle note de {name} : "))
                        if 0 <= note <= 20:
                            time.sleep(1)
                            break
                        print("Erreur, la note doit être comprise entre 0 et 20.")
                        time.sleep(1)
                    except ValueError:
                        print("Erreur, veuillez entrer un nombre entier valide !")
                notes[name] = note
                time.sleep(1)
                print("\nNote mise à jour !\n")
                time.sleep(1)
            else:
                print("Cet élève n'existe pas.")
                time.sleep(1)
    except ValueError:
        print("Veuillez entrer un chiffre\n")
        time.sleep(2)
print("Merci et au revoir !")
time.sleep(2)