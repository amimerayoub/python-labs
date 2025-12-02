# film.py
from dataclasses import dataclass, asdict
import json
from typing import Any
import functools

@functools.total_ordering
@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float  # attendu 0.0 .. 10.0

    def __post_init__(self):
        # validation des bornes de note
        if not (0.0 <= self.note <= 10.0):
            raise ValueError("La note doit être comprise entre 0 et 10.")
        # validation types simples (optionnel)
        if not isinstance(self.annee, int):
            raise TypeError("L'année doit être un entier.")

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, s: str) -> "Film":
        data = json.loads(s)
        titre = data.get("titre")
        realisateur = data.get("realisateur")
        annee = int(data.get("annee"))
        note = float(data.get("note"))
        return cls(titre=titre, realisateur=realisateur, annee=annee, note=note)

    def est_classique(self) -> bool:
        return self.annee < 2000

    # Comparaison naturelle par note (croissante)
    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Film):
            return NotImplemented
        return self.note < other.note
