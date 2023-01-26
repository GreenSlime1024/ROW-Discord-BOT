import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio


class Activity(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Activity cog loaded.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def activiy_task():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                activitys = ["運作平台: Eri24816 租的 server",
                            "ROW 介紹網站: https://greenslime1024.github.io/posts/row/", "我會想念你們的"]
                for i in activitys:
                    await self.bot.change_presence(activity=discord.Game(name=i))
                    await asyncio.sleep(30)

        self.bg_task = self.bot.loop.create_task(activiy_task())


async def setup(bot):
    await bot.add_cog(Activity(bot))
