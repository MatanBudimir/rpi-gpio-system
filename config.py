def channels() -> list:
    return [channel for channel in CHANNELS.keys()]


CHANNELS = {
    18: {'name': 'Light bulb'}
}

HOST = '0.0.0.0'
DEBUG = False
PORT = 5000
