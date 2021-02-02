import discord, config
from discord.ext import commands

class error(commands.Cog, name="Error"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArguments):
            await ctx.send('You are missing required arguments')
            return

    @commands.command()
    async def testing(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"Test passed successfully"
        await ctx.send(embed=e)

        
def setup(bot):
    bot.add_cog(error(bot))
