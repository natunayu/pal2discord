from pal2discord.pal2Client import pal2Client
from discord import Client
import configparser
import os

conf = configparser.ConfigParser()
conf.read('./settings.ini')

print(conf.sections())


print(conf['default']['logs_path'])

client = pal2Client(
        conf['default']['logs_path'],
        conf['default']['service_name'],
        int(conf['default']['channel_id']),
        int(conf['restapi']['restapi_port']),
        conf['restapi']['restapi_user'],
        conf['restapi']['restapi_passwd'],
        )

token=conf['default']['token']
client.run(token)

