from pal2discord.pal2Client import pal2Client
from discord import Client
import configparser

client = pal2Client()

config = configparser.ConfigParser()
config.read('settings.ini')

token=config['default']['token']

client.run(token)

