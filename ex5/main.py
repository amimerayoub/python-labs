# main.py
import sys
from csv_reader import (
    charger_csv,
    CsvException,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
)

def main(chemin):
    try:
        articles = charger_csv(chemin)
    except FichierIntrouvableException as e:
        print(f"Erreur : le fichier spécifié est introuvable ({e}).")
        return 2
    except LigneInvalideException as e:
        print(f"Erreur : format de fichier invalide ({e}).")
        return 3
    except PrixNegatifException as e:
        print(f"Erreur : prix invalide ({e}).")
        return 4
    except CsvException as e:
        print(f"Erreur CSV : {e}")
        return 5
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return 99

    # utilisation "sûre" des données
    print("Articles chargés :", len(articles))
    for a in articles:
        print(f"- {a['id']} | {a['nom']} | {a['prix']:.2f}€")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py chemin/vers/fichier.csv")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
