class Rectangle:
    def __init__(self, longueur, largeur):
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return(self.largeur * self.longueur)
    def peri(self):
        return(self.largeur * 2 + self.longueur * 2)
    def agrandir(self, facteur):
        self.largeur = self.largeur * facteur
        self.longueur = self.longueur * facteur

r = Rectangle(10, 5)


print(r.peri())
print(r.aire())
r.agrandir(2)
print(r.peri())
print(r.aire())

