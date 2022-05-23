# coding: utf-8

# need python3-serial:
# sudo apt install python3-serial
# ou pip3 install pySerial
# need guizero:
# pip3 install guizero
from tkinter import Grid
import serial, time
from guizero import App, PushButton, Text, ListBox

def envoie_buzzer():
    global buzzer_id
    if buzzer_id:
        message = bytes('envoi,' + buzzer_id, 'utf-8')
        s.write(message)
        label.value = "Status: message sent"
    else:
        label.value = "Status: cannot send message"

def change_buzzer(value):
    global buzzer_id
    buzzer_id = value
    label.value = f"Status: buzzer value change to {buzzer_id}"

# definition de la liaison série
port = "/dev/ttyACM0"  # A modifier (voir commande dmesg)

baud = 115200
s = serial.Serial(port)
s.baudrate = baud    

# list des buzzers
buzzer_list = ["0x905ea511","0xbd0fa2a8"]
buzzer_id = ""

# Création de l'application
app = App(title="Microbit Buzzer Tester",layout="grid") 

# Création d'un bouton pour envoyer un message au buzzer
button_buzzer = PushButton(app,text="send Buzzer", command=envoie_buzzer,grid=[0,1])

# Création d'une liste de choix (buzzer identifiant)
listbox = ListBox(
    app,
    items=["0x905ea511","0xbd0fa2a8"],
    command=change_buzzer,
    scrollbar=True, grid=[1,0])

label = Text(app, text="Status: ready", grid=[0,2])

app.display()
