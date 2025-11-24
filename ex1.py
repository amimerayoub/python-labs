import uuid
from datetime import datetime
from copy import deepcopy

class CompteBancaire:
    _ALLOWED_ATTRS = {
        '_titulaire',
        '_CompteBancaire__solde',
        '_operations',
        'id',
        '_initializing'
    }

    def __init__(self, titulaire, solde_initial=0.0):
        object.__setattr__(self, '_initializing', True)
        object.__setattr__(self, 'id', str(uuid.uuid4()))
        object.__setattr__(self, '_titulaire', titulaire)
        object.__setattr__(self, '_CompteBancaire__solde', float(solde_initial))
        object.__setattr__(self, '_operations', [])
        object.__setattr__(self, '_initializing', False)
        self._log_operation("Création compte", solde_initial)

    def __setattr__(self, name, value):
        if getattr(self, '_initializing', False):
            return object.__setattr__(self, name, value)
        if name in self.__dict__:
            return object.__setattr__(self, name, value)
        if name in self._ALLOWED_ATTRS:
            return object.__setattr__(self, name, value)
        raise AttributeError(f"Création d'attribut non autorisée : {name!r}")

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Montant invalide.")
        current = object.__getattribute__(self, '_CompteBancaire__solde')
        new = current + montant
        object.__setattr__(self, '_CompteBancaire__solde', new)
        self._log_operation("Dépôt", montant)

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Montant invalide.")
        current = object.__getattribute__(self, '_CompteBancaire__solde')
        if montant > current:
            raise ValueError("Fonds insuffisants.")
        new = current - montant
        object.__setattr__(self, '_CompteBancaire__solde', new)
        self._log_operation("Retrait", -montant)

    @property
    def solde(self):
        return object.__getattribute__(self, '_CompteBancaire__solde')

    def _log_operation(self, type_op, montant):
        timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
        entry = f"{timestamp} | {type_op} | {montant:+.2f} € | solde={self.solde:.2f}"
        object.__getattribute__(self, '_operations').append(entry)

    def get_operations(self):
        return deepcopy(object.__getattribute__(self, '_operations'))

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde:.2f} € (id={self.id})"


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0.0, taux_annuel=0.02):
        super().__init__(titulaire, solde_initial)
        object.__setattr__(self, '_taux_annuel', float(taux_annuel))

    def calculer_interet(self, periode_annees=1.0, capitaliser=True):
        if periode_annees <= 0:
            raise ValueError("Période invalide.")
        taux = object.__getattribute__(self, '_taux_annuel')
        interets = self.solde * taux * periode_annees
        if capitaliser and interets != 0:
            self.deposer(interets)
            ops = object.__getattribute__(self, '_operations')
            if ops:
                ops[-1] = ops[-1].replace("Dépôt", "Intérêts")
        return interets

    def __str__(self):
        taux = object.__getattribute__(self, '_taux_annuel')
        return f"CompteEpargne Titulaire : {self._titulaire}, Solde : {self.solde:.2f} €, Taux : {taux*100:.2f}%"


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    print(compte)
    compte.deposer(200)
    compte.retirer(150)
    print("Solde accessible :", compte.solde)
    for op in compte.get_operations():
        print(op)

    try:
        compte.solde = 500
    except Exception as e:
        print(repr(e))

    try:
        compte.solde2 = 42
    except Exception as e:
        print(repr(e))

    ce = CompteEpargne("Sana", 2000, 0.03)
    print(ce)
    interets = ce.calculer_interet(1)
    print(interets)
    print(ce)
    for op in ce.get_operations():
        print(op)
