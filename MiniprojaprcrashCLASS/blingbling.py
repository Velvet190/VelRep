import random
import time

symboles = ["🍒", "🍋", "💎"]
solde = 100
play_again = True

while play_again:
    
    print("\n💰 Solde : ", solde)
    time.sleep(0.5)
    try:
        mise = int(input("💵 Combien veux-tu miser ? "))
        if mise > solde:
            print("Vous ne pouvez pas miser plus de ce que vous avez !")
        elif mise <= 0:
            print("Veuillez entrer un montant valide !")
        else:
            solde -= mise
            print("\n\n")
            print("💰 Solde : ", solde)
            print("\n")
            print("💵 Mise : ", mise)
            print("\n")

            a = random.choice(symboles)
            b = random.choice(symboles)
            c = random.choice(symboles)

            print("🎰 |", a, "|", b, "|", c)
            if a == b == c:
                time.sleep(1)
                solde += mise*4
                print("\nJACKPOT 😍🤑🤑")
                print("💰 Solde : ", solde)
            else:
                time.sleep(1)
                print("\nTu as perdu 😭")
                print("💰 Solde : ", solde)
        if solde <= 0:
            print("💀 Tu n'as plus d'argent !\n")
            print("Merci d'avoir joué !")
            play_again = False
            break
        else:
            print("\n1 - Jouer 🎰")
            print("2 - Quitter 🚪\n")
        while True:  
            play_again = input("Votre choix :")
            if play_again == "1":
                play_again = True
                break
            elif play_again == "2":
                print("Merci d'avoir joué !")
                play_again = False
                break
            else:
                print("Veuillez entrer une valeur valide !")
    except ValueError:
        print("Veuillez entrer une valeur valide !")

