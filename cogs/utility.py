import discord, config
from discord.ext import commands

class utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Get someone's ID")
    async def id(self, ctx, member: discord.Member):
        await ctx.send(member.id)


def setup(bot):
    bot.add_cog(utility(bot))
