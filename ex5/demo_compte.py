# demo_compte.py
from compte import CompteBancaire, SoldeInsuffisantException, DepotNegatifException

def demo():
    c = CompteBancaire("Alice", 100.0)
    c.afficher()
    try:
        c.retirer(150)
    except SoldeInsuffisantException as e:
        print("Erreur:", e)

    try:
        c.deposer(-10)
    except DepotNegatifException as e:
        print("Erreur dépôt:", e)

if __name__ == "__main__":
    demo()
