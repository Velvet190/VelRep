class Personnage:
    def __init__(self, name, pv):
        self.name = name
        self.pv = pv
    
    def attaquer(self):
        print(self.name, " attaque !")
    
    def est_vivant(self):
        if self.pv <= 0:
            return False
        else:
            return True

class Guerrier(Personnage):
    def __init__(self, name, pv):
        super().__init__(name, pv)

    def attaquer(self, target):
        print(target.name, "a", target.pv, "!")
        if target.est_vivant():
            print(self.name, "frappe avec son épée !")
            target.pv = target.pv - 20
            print(target.name, "a", target.pv, "!\n")
        else:
            print(target.name, "est deja mort !\n")
    
class Mage(Personnage):
    def __init__(self, name, pv):
        super().__init__(name, pv)

    def attaquer(self, target):
        print(target.name, "a", target.pv, "!")
        if target.est_vivant():
            print(self.name, "lance un sort !")
            target.pv = target.pv - 30
            print(target.name, "a", target.pv, "!\n")
        else:
            print(target.name, "est deja mort !\n")

cible = Guerrier("Garen", 120)

personnages = [
    Guerrier("Arthur", 100),
    Mage("Merlin", 80)
]

for personnage in personnages:
    personnage.attaquer(cible)