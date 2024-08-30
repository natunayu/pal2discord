from discord.ext import commands, tasks
from discord import Intents


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def list(self, ctx: commands.Context) -> None:
        players = self.bot.rAController.get_player_list()
        if players is None:
            await ctx.send("現在ログイン中のプレイヤーはいません")
            return

        text = "```Playerリスト:"
        for player in players:
            text += '\n  ' + player

        text += "```"
        await ctx.send(text)


    @commands.command()
    async def info(self, ctx: commands.Context) -> None:
        text = self.bot.rAController.show_info('info', 'サーバ情報')
        await ctx.send(text)


    @commands.command()
    async def settings(self, ctx: commands.Context) -> None:
        text = self.bot.rAController.show_info('settings', 'サーバ設定')
        await ctx.send(text)


    @commands.command()
    async def metrics(self, ctx: commands.Context) -> None:
        text = self.bot.rAController.show_info('metrics', 'サーバ状態')
        await ctx.send(text)


    @commands.command()
    async def phelp(self, ctx: commands.Context) -> None:
        text = """```
            コマンド一覧:\n  
            !list ログインプレイヤー一覧\n
            !info      サーバ情報\n
            !metrics   サーバ状態\n
            !settings  サーバ設定\n
            !phelp　ヘルプ
            ```
        """
        await ctx.send(text)
