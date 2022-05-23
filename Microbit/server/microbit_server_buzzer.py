# Tigrouroyal
# Microbit server (buzzer), envoie des messages radio
#
from microbit import *
import radio

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

buzzer_numero_serie = '0xbd0fa2a8'
# buzzer_numero_serie_bidon = '0xbd0fa2a9'

# nettoyage au démarrage
display.clear()

# méthode pour envoyer un message pour un buzzer particulier
# grâce à son numéro de série
def envoi(buzzer_parametre):
    #    display.clear()
    display.show(Image.BUTTERFLY)
    message = buzzer_parametre
    radio.send(message)

# boucle
while True:
    if uart.any():
        msg_bytes = uart.read()
        msg_str = str(msg_bytes, 'UTF-8')
        messages = msg_str.split(',')
        if messages[0] == 'envoi':
            if len(messages) > 1:
                buzzer_numero_serie = messages[1]
            envoi(buzzer_numero_serie)
            sleep(2000)
            display.clear()
        else:
            display.show(Image.DIAMOND)
            sleep(1000)
            display.clear()
    sleep(1000)
# fin boucle

