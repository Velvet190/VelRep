import random

class Personnage:
    def __init__(self, name, pv):
        self.name = name
        self.pv = pv
    
    def attaquer(self, target):
        print(target.name, "a", target.pv, "!")
        if target.est_vivant():
            print(self.name, self.msg)
            temp = random.randint(self.degatsmin, self.degatsmax)
            target.pv = target.pv - temp
            print(temp, "dégats !")
            print(target.name, "a", target.pv, "!\n")
            return temp
        else:
            print(target.name, "est deja mort !\n")
            return 0
    
    def est_vivant(self):
        if self.pv <= 0:
            return False
        else:
            return True

    @staticmethod
    def afficher_personnages(personnages):
        for perso in personnages:
            print(perso.name, "-", perso.pv, "PV")

class Guerrier(Personnage):
    def __init__(self, name, pv):
        super().__init__(name, pv)
        self.degatsmin = 15
        self.degatsmax = 25
        self.msg = "frappe avec son épée !"

    
class Mage(Personnage):
    def __init__(self, name, pv):
        super().__init__(name, pv)
        self.degatsmin = 30
        self.degatsmax = 45
        self.msg = "lance un sort !"


garen = Guerrier("Garen", 100)
arthur = Guerrier("Arthur", 100)
merlin = Mage("Merlin", 80)
tour = 1


while True:
    print("\n========== TOUR", tour, "==========\n")
    if arthur.est_vivant():
        arthur.attaquer(garen)
    if garen.est_vivant():
        if merlin.est_vivant():
            merlin.attaquer(garen)
        if garen.est_vivant():
            garen.attaquer(arthur)
            if not arthur.est_vivant() and not merlin.est_vivant():
                print("Arthur et Merlin sont morts !")
                print("Garen a gagné !")
                break
        else:
            if arthur.est_vivant():
                print("Garen est mort")
                print("Arthur et Merlin ont gagnés !")
                break
            else:
                print("Garen et Arthur sont morts !")
                print("Merlin a gagné !")
                break
    else:
        if merlin.est_vivant():
            print("Garen est mort")
            print("Arthur et Merlin ont gagnés !")
            break
        else:
            print("Garen et Merlin sont morts !")
            print("Arthur a gagné !")
            break
    tour += 1