# formes.py
from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def aire(self) -> float:
        """Retourne l'aire de la forme"""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"

class Cercle(Forme):
    def __init__(self, rayon: float):
        if rayon < 0:
            raise ValueError("Le rayon doit être positif")
        self.rayon = rayon

    def aire(self) -> float:
        return math.pi * self.rayon ** 2

class Rectangle(Forme):
    def __init__(self, largeur: float, hauteur: float):
        if largeur < 0 or hauteur < 0:
            raise ValueError("Dimensions positives requises")
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self) -> float:
        return self.largeur * self.hauteur

class Triangle(Forme):
    def __init__(self, base: float, hauteur: float):
        if base < 0 or hauteur < 0:
            raise ValueError("Dimensions positives requises")
        self.base = base
        self.hauteur = hauteur

    def aire(self) -> float:
        return 0.5 * self.base * self.hauteur

# Extension : Carré dérivé de Rectangle
class Carre(Rectangle):
    def __init__(self, cote: float):
        if cote < 0:
            raise ValueError("Côté doit être positif")
        super().__init__(cote, cote)

# Extension : mixin pour la couleur
class ColorMixin:
    def __init__(self, couleur: str = "sans couleur", *args, **kwargs):
        self.couleur = couleur
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        # utilise le __str__ de Forme (via MRO)
        base = super().__str__()
        return f"{base} — couleur : {self.couleur}"

# Exemple d'une forme colorée
class CercleColore(ColorMixin, Cercle):
    def __init__(self, rayon: float, couleur: str = "rouge"):
        # ColorMixin -> Cercle
        super().__init__(couleur=couleur, rayon=rayon)

# Démo
def demo():
    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2),
        Carre(5),
        CercleColore(2, couleur="bleu")
    ]
    for f in formes:
        print(f)

if __name__ == "__main__":
    demo()
