from os import getenv
from discord import Client, Intents, Interaction
from discord.ext import tasks
from discord.app_commands import (
    CommandTree,
    allowed_installs, guild_install, user_install,
    allowed_contexts, dm_only, guild_only, private_channel_only,
)
import logManager


class pal2Client(Client):
    def __init__(self):
        super().__init__(intents=Intents.default())
        self.tree = CommandTree(self)
        self.logManager = logManager

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    @tasks.loop(seconds=1)
    async def loop(log_path, svc_name):
        


