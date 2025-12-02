# tache_squelett.py
from datetime import datetime
from typing import List, Tuple
import copy

class TitreInvalideException(Exception):
    """Lever quand le titre est manquant ou vide."""
    pass

class ValidationMixin:
    def valider_titre(self) -> None:
        """
        Vérifie que self.titre est une chaîne non vide.
        Lève TitreInvalideException si invalide.
        """
        raise NotImplementedError("Implémentez valider_titre dans votre mixin")

class HistoriqueMixin:
    def __init__(self, *args, **kwargs):
        """
        Initialise l'historique. Appeler super().__init__(*args, **kwargs) dans la classe concrète.
        """
        self.historique: List[Tuple[datetime, str]] = []
        # Ne pas appeler raise ici — c'est un mixin d'initialisation
        super().__init__(*args, **kwargs)

    def enregistrer_etat(self) -> None:
        """
        Enregistre la description courante avec timestamp.
        """
        raise NotImplementedError("Implémentez enregistrer_etat")

    def afficher_historique(self) -> None:
        """
        Affiche ou retourne l'historique.
        """
        raise NotImplementedError("Implémentez afficher_historique")

class JournalisationMixin:
    def journaliser(self, message: str) -> None:
        """
        Journalise l'action (affiche dans la console avec timestamp).
        """
        raise NotImplementedError("Implémentez journaliser")

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre: str, description: str):
        """
        Initialise la tâche :
        - set titre, description
        - set date_creation
        - appeler les init de mixins si nécessaire (HistoriqueMixin prend super().__init__)
        - valider le titre
        - journaliser la création
        """
        # Exemple d'initialisation standard — adaptez selon votre implémentation des mixins
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()
        # Assurez-vous d'appeler l'init des mixins si nécessaire :
        try:
            super().__init__()  # permet d'exécuter Historicable.__init__
        except TypeError:
            # Si vos mixins n'ont pas d'__init__ acceptant aucun argument,
            # ignorez ou adaptez selon votre design.
            pass

        # validation
        self.valider_titre()
        # journaliser création
        self.journaliser(f"Tâche créée : '{self.titre}'")

    def mettre_a_jour(self, nouvelle_description: str) -> None:
        """
        1. valider titre
        2. enregistrer état courant
        3. mettre à jour description
        4. journaliser
        """
        raise NotImplementedError("Implémentez mettre_a_jour")

    # Vous pouvez déléguer afficher_historique à HistoriqueMixin
