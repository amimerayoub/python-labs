# compte.py
import logging

# Logger simple (optionnel) — écriture dans compte_errors.log
logger = logging.getLogger("compte")
if not logger.handlers:
    h = logging.FileHandler("compte_errors.log", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    h.setFormatter(formatter)
    logger.addHandler(h)
    logger.setLevel(logging.INFO)


class SoldeInsuffisantException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DepotNegatifException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class CompteBancaire:
    def __init__(self, nom: str, solde: float = 0.0):
        self.nom = nom
        self.solde = float(solde)

    def deposer(self, montant: float) -> None:
        if montant <= 0:
            msg = f"Tentative de dépôt invalide ({montant}) pour {self.nom}"
            logger.warning(msg)
            raise DepotNegatifException("Le montant du dépôt doit être strictement positif.")
        self.solde += montant
        logger.info(f"Dépôt de {montant:.2f}€ sur le compte {self.nom}. Nouveau solde: {self.solde:.2f}€")

    def retirer(self, montant: float) -> None:
        if montant <= 0:
            msg = f"Tentative de retrait invalide ({montant}) pour {self.nom}"
            logger.warning(msg)
            raise ValueError("Le montant du retrait doit être strictement positif.")
        if montant > self.solde:
            msg = f"Retrait refusé: {montant:.2f}€ > solde {self.solde:.2f}€ pour {self.nom}"
            logger.error(msg)
            raise SoldeInsuffisantException("Solde insuffisant pour ce retrait.")
        self.solde -= montant
        logger.info(f"Retrait de {montant:.2f}€ sur le compte {self.nom}. Nouveau solde: {self.solde:.2f}€")

    def solde_actuel(self) -> float:
        return self.solde

    # méthode d'affichage utile pour demo / CLI — n'est pas utilisée dans la logique métier
    def afficher(self) -> None:
        print(f"Compte: {self.nom}, Solde: {self.solde:.2f}€")
