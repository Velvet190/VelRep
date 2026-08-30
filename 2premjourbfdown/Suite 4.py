notes = {
    "Alice": 15,
    "Bob": 8
}

sortie = {}

def sauvegarder_notes(notes):
    with open("notes.txt", "w") as fichier:
        for name, note in notes.items():
            fichier.write(name)
            fichier.write(":")
            fichier.write(str(note))
            fichier.write("\n")

def charger_notes():
    with open("notes.txt", "r") as fichier:
        for ligne in fichier:
            coupage = ligne.split(":")
            name = coupage[0]
            note = int(coupage[1])
            sortie[name] = note



sauvegarder_notes(notes)
charger_notes()
print(notes)
print("\n\n")
print(sortie)
