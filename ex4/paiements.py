# paiements.py
from abc import ABC, abstractmethod
from typing import List
import random

def _format_montant(montant: float) -> str:
    return f"{montant:.2f}€"

def _luhn_valide(numero: str) -> bool:
    """Vérification Luhn simplifiée — accepte chiffres et espaces"""
    digits = [int(ch) for ch in numero if ch.isdigit()]
    if len(digits) < 12:  # exigence minimale pour l'exercice
        return False
    # Luhn algorithm
    s = 0
    alt = False
    for d in reversed(digits):
        if alt:
            d = d * 2
            if d > 9:
                d -= 9
        s += d
        alt = not alt
    return s % 10 == 0

class Paiement(ABC):
    def __init__(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._montant = float(montant)

    @abstractmethod
    def payer(self) -> str:
        """Doit retourner une chaîne de confirmation"""
        pass

class CarteBancaire(Paiement):
    def __init__(self, montant: float, numero: str, cvv: str):
        super().__init__(montant)
        self.numero = numero.replace(" ", "")
        self.cvv = cvv
        if not _luhn_valide(self.numero):
            raise ValueError("Numéro de carte invalide (Luhn échoué)")
        if not (self.cvv.isdigit() and 3 <= len(self.cvv) <= 4):
            raise ValueError("CVV invalide")

    def payer(self) -> str:
        # Simule un paiement et renvoie un message
        token = f"CB-{self.numero[-4:]}-{random.randint(1000,9999)}"
        return (f"Paiement par CarteBancaire de {_format_montant(self._montant)} "
                f"confirmé (token {token})")

class PayPal(Paiement):
    def __init__(self, montant: float, email: str, token_api: str):
        super().__init__(montant)
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email PayPal invalide")
        self.email = email
        self.token_api = token_api

    def payer(self) -> str:
        # Simule appel API
        ref = f"PP-{self.email.split('@')[0]}-{random.randint(1000,9999)}"
        return (f"Paiement via PayPal de {_format_montant(self._montant)} "
                f"effectué (réf {ref})")

class Crypto(Paiement):
    def __init__(self, montant: float, wallet_id: str, reseau: str):
        super().__init__(montant)
        if not wallet_id:
            raise ValueError("Wallet ID requis")
        if reseau.upper() not in {"BTC", "ETH", "LTC", "BSC"}:
            # on autorise quelques réseaux pour l'exemple
            raise ValueError("Réseau crypto non supporté")
        self.wallet_id = wallet_id
        self.reseau = reseau.upper()

    def payer(self) -> str:
        # Simule broadcast de transaction
        txid = f"{self.reseau[:3]}-{random.randint(10**7,10**8-1)}"
        return (f"Paiement en {self.reseau} de {_format_montant(self._montant)} "
                f"envoyé (tx {txid})")

def traiter_paiements(liste_paiements: List[ Paiement ]) -> List[str]:
    """
    Parcourt la liste et appelle payer() sur chaque objet.
    Ne fait pas de isinstance: fait confiance au polymorphisme.
    Renvoie la liste des confirmations.
    """
    confirmations = []
    for p in liste_paiements:
        try:
            confirmations.append(p.payer())
        except Exception as e:
            confirmations.append(f"Échec du paiement : {e}")
    return confirmations

def demo():
    # créer des exemples valides
    paiements = [
        CarteBancaire(25.5, "4539 1488 0343 6467", "123"),  # exemple Luhn valide
        CarteBancaire(10.0, "4716 6210 1100 0000", "321"),  # autre exemple
        PayPal(15.0, "alice@example.com", "token-xyz-1"),
        PayPal(7.25, "bob.smith@mail.org", "token-abc-2"),
        Crypto(0.005, "wallet-123", "BTC"),
        Crypto(0.2, "wallet-xyz", "ETH")
    ]

    confirmations = traiter_paiements(paiements)
    for c in confirmations:
        print(c)

if __name__ == "__main__":
    demo()
