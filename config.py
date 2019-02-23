import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['CLIENT_ID']
client_secret = config['CLIENT_SECRET']