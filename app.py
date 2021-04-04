from flask import Flask, Blueprint, jsonify, request
import RPi.GPIO as GPIO
import config

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(config.channels(), GPIO.OUT, initial=GPIO.HIGH)


@app.route('/output/<int:gpio_id>')
def gpio_switch(gpio_id: int):
    try:
        GPIO.output(gpio_id, not GPIO.input(gpio_id))
        return jsonify({'success': True, 'message': f'{config.CHANNELS[gpio_id]["name"]} was turned on.' if not GPIO.input(gpio_id) else f'{config.CHANNELS[gpio_id]["name"]} was turned off.'})
    except Exception as exception:
        return jsonify({'success': False, 'message': exception.__str__()})


@app.route('/output/register', methods=['POST'])
def gpio_register():
    data = request.get_json()

    if 'name' not in data or 'channel' not in data:
        return jsonify({'success': False, 'message': "Make sure all data is present."}), 400
    elif type(data['channel']) is not int:
        return jsonify({'success': False, 'message': "Channel has to be a number."}), 400
    
    name = data['name']
    channel = data['channel']

    if channel < 1 or channel > 40:
        return jsonify({'success': False, 'message': "Channel has to be equal or bigger than 1." if channel < 1 else "Channel has to be equal or lower than 40."}), 400

    return jsonify(data)

try:
    app.run(debug=config.DEBUG, port=config.PORT, host=config.HOST, threaded=True)
finally:
    GPIO.cleanup()
