# reservation.py
import logging

logger = logging.getLogger("reservation")
if not logger.handlers:
    h = logging.FileHandler("reservation.log", encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    h.setFormatter(fmt)
    logger.addHandler(h)
    logger.setLevel(logging.INFO)


class ReservationException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class CapaciteDepasseeException(ReservationException):
    pass


class NombreInvalideException(ReservationException):
    pass


class NomClientInvalideException(ReservationException):
    pass


class Evenement:
    def __init__(self, nom: str, capacite: int):
        if capacite < 0:
            raise ValueError("La capacité doit être >= 0")
        self.nom = nom
        self.capacite = int(capacite)
        self.places_reservees = 0

    def reserver(self, nom_client: str, nb_places: int) -> None:
        # Validation des paramètres métier
        if not isinstance(nom_client, str) or not nom_client.strip():
            logger.warning("Nom client invalide lors d'une tentative de réservation.")
            raise NomClientInvalideException("Nom du client requis.")
        if not isinstance(nb_places, int) or nb_places <= 0:
            logger.warning("Nombre de places invalide: %s", nb_places)
            raise NombreInvalideException("Nombre de places invalide.")
        if self.places_reservees + nb_places > self.capacite:
            logger.warning("Capacité dépassée: %s requested, %s reserved/%s cap",
                           nb_places, self.places_reservees, self.capacite)
            raise CapaciteDepasseeException("Capacité dépassée.")

        self.places_reservees += nb_places
        logger.info("Réservation confirmée: %s (%d places).", nom_client, nb_places)

    def afficher(self) -> None:
        print(f"Événement: {self.nom} — {self.places_reservees}/{self.capacite} places réservées")
