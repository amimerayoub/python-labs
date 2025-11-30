# animaux.py
from typing import Iterable

class Animal:
    def parler(self) -> str:
        """Interface : doit être surchargée par les sous-classes"""
        raise NotImplementedError("Cette méthode doit être redéfinie")

class Chien(Animal):
    def parler(self) -> str:
        return "Ouaf !"

class Chat(Animal):
    def parler(self) -> str:
        return "Miaou !"

class Vache(Animal):
    def parler(self) -> str:
        return "Meuh !"

# Ne dérive PAS d'Animal — montre le duck typing
class Robot:
    def parler(self) -> str:
        return "Bip bop — je parle comme un robot."

def faire_parler(animal_like) -> None:
    """Accepte tout objet qui fournit parler() — duck typing"""
    print(animal_like.parler())

def demo():
    animaux: Iterable = [Chien(), Chat(), Vache(), Robot(), Chien()]
    for a in animaux:
        faire_parler(a)

if __name__ == "__main__":
    demo()
