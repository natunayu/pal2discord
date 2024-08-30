from os import getenv
from discord import Client, Intents, Interaction
from discord.ext import tasks
from discord.app_commands import (
    CommandTree,
    allowed_installs, guild_install, user_install,
    allowed_contexts, dm_only, guild_only, private_channel_only,
)
from pal2discord.logManager import logManager
from pal2discord.restApiController import restApiController


class pal2Client(Client):
    def __init__(self, 
            log_path, svc_name, cha_id,
            port, user, passwd
            ):

        intents = Intents.default()
        intents.message_content = True 
        super().__init__(intents=intents)
        
        self.tree = CommandTree(self)
        self.channel_id = cha_id
        self.logManager = logManager(log_path, svc_name)
        self.rAController = restApiController(port, user, passwd)

        
    async def setup_hook(self) -> None:
        await self.tree.sync()


    async def on_ready(self):
        print(f'Logged on as {self.user}')
        channel = self.get_channel(self.channel_id)
        #await channel.send('パルワールドサーバが起動しました！')
        self.log_loop.start()


    async def on_message(self, message):
        if message.author.bot or message.channel.id != self.channel_id:
            return
        
        self.rAController.send_msg(message.author.display_name, message.content)


    @tasks.loop(seconds=1)
    async def log_loop(self):
        msg = self.logManager.get_latest_pal_chat()
        if msg:
            channel = self.get_channel(self.channel_id)
            await channel.send(msg)


