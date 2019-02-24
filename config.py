import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['CLIENT']['CLIENT_ID']
client_secret = config['CLIENT']['CLIENT_SECRET']
plotly_user = config['PLOTLY']['PLOTLY_USER']
plotly_api_key = config['PLOTLY']['PLOTLY_API_KEY']

print("client id: ", client_id)
print("client secret: ", client_secret)