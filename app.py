from flask import Flask
import RPi.GPIO as GPIO
from config import channels

app = Flask(__name__)

GPIO.set(GPIO.BOARD)
GPIO.setup(channels(), GPIO.OUT)


@app.route('/')
def hello_world():
    GPIO.output(18, not GPIO.input(18))
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
