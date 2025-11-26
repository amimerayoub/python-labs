from employes import Employe
from managers_devs import Manager, Developpeur
from document import Livre, Magazine

if __name__ == '__main__':
    # Exercice 1 : employés
    e = Employe("Alice", 2000)
    m = Manager("Bob", 2500, 800)
    d = Developpeur("Charlie", 2200, "Python")

    for personne in [e, m, d]:
        print(personne)

    print()  # séparation

    # Exercice 2 : bibliothèque
    docs = [
        Livre("1984", 1949, "George Orwell"),
        Magazine("Science & Vie", 2023, 456),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
    ]

    for doc in docs:
        doc.afficher()