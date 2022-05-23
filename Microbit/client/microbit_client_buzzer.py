# Tigrouroyal
# Microbit client (buzzer), écoute radio
#
from microbit import *
import machine
import radio
import time

# récupérer mon numéro de série
def get_serial_number(type=hex):
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25  # deviceid[1]
    return type(machine.mem32[NRF_FICR_BASE + (DEVICEID_INDEX*4)] & 0xFFFFFFFF)

# stocker le numéro de série dans une variable: chaine de caractères
numero_serie = get_serial_number()

# configuration radio:
# radio.config(channel=XX) (defaut=7) valeur entre 0 et 83
# radio.config(address=0x75626974) (defaut=0x75626974) filtre des paquets entrants
# radio.config(group=0) (defaut=0) valeur entre 0 et 255
# radio.config(power=6) (defaut=6) puissance d'émission du signal (allant de 0 à 7)
# radio.config(queue=3) nombre de messages dans la file d'attente.
#   Au delà de 3 messages en attente, ils seront supprimés.
# radio.config(length=32) longueur maximum du message. Celle-ci peut aller jusqu'à 251.
# radio.config(data_rate=radio.RATE_1MBIT) vitesse de transmission.
#       Les vitesses admissibles sont RATE_250KBIT, RATE_1MBIT ou RATE_2MBIT

# activer la radio avec les valeurs de configuration par défaut
radio.on()

# boucle infinie de gestion des messages entrants
while True:
    paquetentrant = radio.receive()
    # vérifier que le paquet entrant n'est pas vide (None)
    if paquetentrant:
        # afficher témoin de message
        display.show(Image.DIAMOND)
        sleep(500)
        # effacer l'écran
        display.clear()
        # si la valeur du paquet entrant correspont à mon numéro de série
        if paquetentrant == numero_serie:
            # faire afficher, vibrer, sonner pendant 5 secondes
            stop = time.ticks_add(time.ticks_ms(), 5000)
            # alors afficher message, faire sonner et vibrer le buzzer
            display.show(Image.HAPPY)
            while time.ticks_diff(stop, time.ticks_ms()) > 0:
                # attendre un peu: 1/2 secondes
                sleep(500)
            # fin boucle
            # effacer l'écran
            display.clear()
# fin de la boucle infinie
