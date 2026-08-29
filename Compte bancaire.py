class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant

class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde, taux):
        super().__init__(titulaire, solde)
        self.taux = taux
    def interet(self):
        self.solde += self.solde * self.taux
    def retirer(self, montant):
        if montant <= self.solde - 10:
            self.solde -= montant


compte = CompteEpargne("José", 100, 0.05)

compte.interet()
compte.retirer(95)
print(compte.solde)