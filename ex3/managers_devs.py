from employes import Employe

class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        super().__init__(nom, salaire_base)
        self.prime = prime

    def salaire_total(self):
        return self.salaire_base + self.prime

class Developpeur(Employe):
    def __init__(self, nom, salaire_base, technologie):
        super().__init__(nom, salaire_base)
        self.technologie = technologie

    def salaire_total(self):
        bonus = 500 if self.technologie == 'Python' else 300
        return self.salaire_base + bonus