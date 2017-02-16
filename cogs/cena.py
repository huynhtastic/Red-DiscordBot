import discord
from discord.ext import commands
from random import randint
import aiohttp
import random

class Cena:
    """Image related commands."""

    def __init__(self, bot):
        self.bot = bot
        #Reserved for further ... stuff

    """Commands section"""

    @commands.command(no_pm=True)
    async def mayo(self, user : discord.Member):
        await self.bot.say(user.mention)

    @commands.command(no_pm=True)
    async def thang(self):
        await self.bot.say("Just fucking https://www.google.com it THANG")
        """Retrieves a picture from imgur

        imgur search [keyword] - Retrieves first hit of search query.
        imgur [subreddit section] [top or new] - Retrieves top 3 hottest or latest pictures of today for given a subreddit section, e.g. 'funny'."""
        # imgurclient = ImgurClient("1fd3ef04daf8cab", "f963e574e8e3c17993c933af4f0522e1dc01e230")
        # if text == ():
        #     rand = randint(0, 59) #60 results per generated page
        #     items = imgurclient.gallery_random(page=0)
        #     await self.bot.say(items[rand].link)
        # elif text[0] == "search":
        #     items = imgurclient.gallery_search(" ".join(text[1:len(text)]), advanced=None, sort='time', window='all', page=0)
        #     if len(items) < 1:
        #         await self.bot.say("Your search terms gave no results.")
        #     else:
        #         await self.bot.say(items[0].link)
        # elif text[0] != ():
        #     try:
        #         if text[1] == "top":
        #             imgSort = "top"
        #         elif text[1] == "new":
        #             imgSort = "time"
        #         else:
        #             await self.bot.say("Only top or new is a valid subcommand.")
        #             return
        #         items = imgurclient.subreddit_gallery(text[0], sort=imgSort, window='day', page=0)
        #         if (len(items) < 3):
        #             await self.bot.say("This subreddit section does not exist, try 'funny'")
        #         else:
        #             await self.bot.say("{} {} {}".format(items[0].link, items[1].link, items[2].link))
        #     except:
        #         await self.bot.say("Type help imgur for details.")


def setup(bot):
    bot.add_cog(Cena(bot))