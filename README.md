# Spotify Interactive Map
by the hAcKiLlinOis2019Squad (Amanda Wang, Charles Kuch, and Japneet Singh)

This is an interactive web map of artists and albums pulled from the Spotify API.
Our project uses [Spotipy](https://spotipy.readthedocs.io/en/latest/) and [Flask](http://flask.pocoo.org/docs/1.0/).

Our deployment is displayed here on [Heroku](https://spotify-interactive-map-19.herokuapp.com/).

## Installation & Setup
1. Please have this Repository cloned by running:
`git clone https://github.com/CandyMandy28/hAcKiLlinOis2019Squad`

1. Run in your terminal:
`pip install -r requirements.txt`

2. Duplicate and rename `config_example.ini` to `config.ini`

3. If you have Spotify Premium, please go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

3. Create a Spotify App, and get your Client ID and Client Secret. Copy those tokens into your `config.py`

3. You should be done with setup!

4. Run `main.py` in a server of sorts like Heroku.

*This will execute the `main.py` file with the environment variables.*