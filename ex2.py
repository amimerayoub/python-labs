import uuid
from datetime import datetime

class CompteBancaire:
    def __init__(self, solde_initial=0.0):
        self.id = str(uuid.uuid4())
        self.__solde = solde_initial
        self._operations = []
        self._log("Création", solde_initial)

    def _log(self, type_op, montant):
        t = datetime.now().isoformat(sep=" ", timespec="seconds")
        self._operations.append(f"{t} | {type_op} | {montant:+.2f} € | solde={self.__solde:.2f}")

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._log("Dépôt", montant)

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._log("Retrait", -montant)

    def get_solde(self):
        return self.__solde

    def get_operations(self):
        return list(self._operations)

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, compte=None):
        if compte is None:
            compte = CompteBancaire()
        self.comptes.append(compte)
        return compte

    def afficher(self):
        for c in self.comptes:
            print(f"Client : {self.nom}, Compte : {c.id}, Solde : {c.get_solde()}€")
#####main.py
client = Client("ayoub")

c1 = client.ajouter_compte()
c1.deposer(300)
c1.retirer(50)

c2 = client.ajouter_compte()
c2.deposer(500)

client.afficher()

print("--- Historique compte 1 ---")
for op in c1.get_operations():
    print(op)

