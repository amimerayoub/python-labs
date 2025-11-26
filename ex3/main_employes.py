from employes import Employe
from managers_devs import Manager, Developpeur

if __name__ == '__main__':
    e = Employe("Alice", 2000)
    m = Manager("Bob", 2500, 800)
    d = Developpeur("Charlie", 2200, "Python")

    for personne in [e, m, d]:
        print(personne)