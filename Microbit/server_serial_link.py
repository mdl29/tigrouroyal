# coding: utf-8
import serial, time
from guizero import App, PushButton, Text

def envoie_buzzer():
    s.write(b'envoi')

def envoie_bidon():
    s.write(b'bidon')

port = "/dev/ttyACM0"  # A modifier (voir commande dmesg)

baud = 115200
s = serial.Serial(port)
s.baudrate = baud    
    
app = App(title="Microbit Buzzer Tester",layout="grid") 

# Création d'un bouton pour envoyer un message au buzzer
button_buzzer = PushButton(app,text="send Buzzer", command=envoie_buzzer,grid=[0,1])

# Création d'un bouton pour envoyer un message bidon au buzzer
button_bidon = PushButton(app,text="send Bidon", command=envoie_bidon,grid=[0,2])

app.display()
