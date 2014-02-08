from flask import Flask, request
from flask.ext.restful import Resource, Api
from pyduino import Arduino
from time import sleep

app = Flask(__name__)
api = Api(app)
connection_delay = 5 # Seconds to wait for the serial connection
pin_mode_change_delay = 0.5 # Seconds to wait for a digital pin mode change

class Digital(Resource):

    def get(self, pin_number):
        a.set_pin_mode(pin_number, 'I')
        sleep(pin_mode_change_delay )
        value = a.digital_read(pin_number)
        return {pin_number : value}

    def put(self, pin_number):
        a.set_pin_mode(pin_number, 'O')
        sleep(pin_mode_change_delay )
        value = request.form['value'] 
        a.digital_write(pin_number, value)
        return {pin_number : value}

api.add_resource(Digital, '/digital/<int:pin_number>')

class Analog(Resource):

    def get(self, pin_number):
        value = a.analog_read(pin_number)
        return {pin_number : value}

    def put(self, pin_number):
        value = request.form['value'] 
        a.analog_write(pin_number, value)
        return {pin_number : value}

api.add_resource(Analog, '/analog/<int:pin_number>')

if __name__ == '__main__':
    a = Arduino()
    sleep(connection_delay)
    app.run(debug=True)
