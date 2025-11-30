# csv_reader.py
import csv
import logging
from typing import List, Dict

logger = logging.getLogger("csv_reader")
if not logger.handlers:
    h = logging.FileHandler("erreurs_csv.log", encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    h.setFormatter(fmt)
    logger.addHandler(h)
    logger.setLevel(logging.INFO)


class CsvException(Exception):
    def __init__(self, message: str, ligne: int = None):
        if ligne is not None:
            super().__init__(f"Ligne {ligne}: {message}")
        else:
            super().__init__(message)
        self.ligne = ligne


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin: str) -> List[Dict[str, object]]:
    """
    Lit un CSV attendu au format: id;nom;prix
    Retourne une liste de dicts: {"id": str, "nom": str, "prix": float}
    Lève:
      - FichierIntrouvableException
      - LigneInvalideException
      - PrixNegatifException
    """
    result = []
    try:
        with open(chemin, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for idx, row in enumerate(reader, start=1):
                # Ignorer les lignes vides (toutes colonnes vides ou longueur 0)
                if not row or all(cell.strip() == "" for cell in row):
                    logger.debug("Ignorée: ligne vide %d", idx)
                    continue

                if len(row) != 3:
                    logger.error("Format incorrect sur la ligne %d: %s", idx, row)
                    raise LigneInvalideException("Nombre de colonnes attendu: 3 (id;nom;prix).", ligne=idx)

                id_str, nom, prix_str = row
                id_str = id_str.strip()
                nom = nom.strip()
                prix_str = prix_str.strip()

                if not id_str:
                    logger.error("ID manquant à la ligne %d", idx)
                    raise LigneInvalideException("ID manquant.", ligne=idx)
                if not nom:
                    logger.error("Nom manquant à la ligne %d", idx)
                    raise LigneInvalideException("Nom manquant.", ligne=idx)

                try:
                    prix = float(prix_str)
                except ValueError:
                    logger.error("Prix non numérique à la ligne %d: %s", idx, prix_str)
                    raise LigneInvalideException("Le prix doit être un nombre.", ligne=idx)

                if prix <= 0:
                    logger.error("Prix négatif ou nul à la ligne %d: %s", idx, prix)
                    raise PrixNegatifException("Le prix doit être strictement positif.", ligne=idx)

                result.append({"id": id_str, "nom": nom, "prix": prix})
    except FileNotFoundError:
        logger.exception("Fichier non trouvé: %s", chemin)
        raise FichierIntrouvableException(f"Fichier introuvable: {chemin}")

    return result
