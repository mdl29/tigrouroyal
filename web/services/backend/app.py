# coding: utf-8
# services Web
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

# Liaison série avec la Microbit server buzzer
# https://pyserial.readthedocs.io/en/latest/pyserial.html
import serial

# configuration
# debug requests (in web page or insomnia)
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# the vuejs is started using another server
# to request Tigrouroyal API from Vuesjs (axios), CORS must be enabled.
CORS(app, resources={r'/*': {'origins': '*'}})

# definition de la liaison série
port = "/dev/ttyACM0"  # A modifier/configurer (voir commande dmesg)

baud = 115200
# configure et ouvre le port série.
# si ça ne marche pas : SerialException est lévée
s = serial.Serial(port)
s.baudrate = baud

# some default values for the buzzer
buzzer_1 = {
    "id": "0xbd0fa2a8",
    "nom": "jac1"
}
buzzer_2 = {
    "id": "0x905ea511",
    "nom": "jac2"
}
buzzer_list = [ buzzer_1, buzzer_2 ]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# get buzzers
@app.route('/api/buzzer', methods=['GET'])
def get_buzzer_list():
    return jsonify(buzzer_list)

# add buzzer
@app.route('/api/buzzer', methods=['POST'])
def add_buzzer():
    buzzer_content = request.json
    print(buzzer_content)
    # if empty fields
    if not buzzer_content["id"]:
        abort(400)
    if not buzzer_content["nom"]:
        abort(400)
    # if already exist
    for one_buzzer in buzzer_list:
        if one_buzzer["id"] == buzzer_content["id"]:
            abort(409)
    # add the new valid buzzer to the list
    buzzer_list.append(buzzer_content)
    return jsonify(buzzer_list)

# delete buzzer
@app.route('/api/buzzer/<buzzer_id>', methods=['DELETE'])
def delete_buzzer(buzzer_id):
    for one_buzzer in buzzer_list:
        if one_buzzer["id"] == buzzer_id:
            buzzer_list.remove(one_buzzer)
    return jsonify(buzzer_list)

# get one buzzer
@app.route('/api/buzzer/<buzzer_id>', methods=['GET'])
def get_buzzer(buzzer_id):
    for one_buzzer in buzzer_list:
        if one_buzzer["id"] == buzzer_id:
            return jsonify(one_buzzer)
    # not found
    abort(404)

# activate one buzzer
@app.route('/api/buzzer/activate/<buzzer_id>', methods=['GET'])
def activate_buzzer(buzzer_id):
    for one_buzzer in buzzer_list:
        if one_buzzer["id"] == buzzer_id:
            print(f"Buzzer activated: {buzzer_id}")
            # envoie le message sur la Microbit server buzzer
            message = bytes('envoi,' + buzzer_id, 'utf-8')
            s.write(message)
            return jsonify(one_buzzer), 204
    # not found
    abort(404)


if __name__ == '__main__':
    app.run()
