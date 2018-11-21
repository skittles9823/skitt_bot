class Config(object):
    LOGGER = True

    API_KEY = "Bot token goes here"
    WEBHOOK = False
    LISTEN = "127.0.0.1" #ip to losten for webhooks
    URL = None
    CERT_PATH = None
    PORT = 5000
    DEEPFRY_TOKEN = None # Used for facial recognition in the deepfry command

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True