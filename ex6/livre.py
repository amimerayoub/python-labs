# livre.py
from dataclasses import dataclass, asdict, replace
import json
from typing import Any
import functools

@functools.total_ordering
@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self) -> str:
        """Sérialise en JSON (utf-8 friendly)."""
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, s: str) -> "Livre":
        """Reconstruit un Livre depuis une chaîne JSON."""
        data = json.loads(s)
        # validations simples
        titre = data.get("titre")
        auteur = data.get("auteur")
        annee = int(data.get("annee"))
        prix = float(data.get("prix"))
        return cls(titre=titre, auteur=auteur, annee=annee, prix=prix)

    def promo(self, prix_reduit: float) -> "Livre":
        """
        Retourne un nouveau Livre identique sauf le prix modifié.
        L'objet original reste inchangé grâce à frozen=True.
        """
        if prix_reduit < 0:
            raise ValueError("Le prix réduit doit être positif ou nul.")
        return replace(self, prix=float(prix_reduit))

    # Comparaison basée uniquement sur le prix (ordre croissant)
    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Livre):
            return NotImplemented
        return self.prix < other.prix
