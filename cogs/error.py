import discord, config
from discord.ext import commands

class error(commands.Cog, name="Error"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArguments):
            await ctx.send('You are missing required arguments')
        else:
            await ctx.send(embed=discord.Embed(title="An error occured", description=str(error))

    @commands.command()
    async def testing(self, ctx, *, sentence):
        await ctx.send(sentence)

        
def setup(bot):
    bot.add_cog(error(bot))
