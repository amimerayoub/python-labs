# demo_reservation.py
from reservation import Evenement, ReservationException

def demo():
    event = Evenement("Concert", 5)
    try:
        event.reserver("", 2)
    except ReservationException as e:
        print("Erreur:", e)

if __name__ == "__main__":
    demo()
