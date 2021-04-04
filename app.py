from flask import Flask, Blueprint
import RPi.GPIO as GPIO
import config

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(config.channels(), GPIO.OUT)


@app.route('/')
def hello_world():
    GPIO.output(18, not GPIO.input(18))
    return 'Hello World!'


app.run(debug=config.DEBUG, port=config.PORT, host=config.HOST, threaded=True)
