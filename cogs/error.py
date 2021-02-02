import discord, config
from discord.ext import commands

class error(commands.Cog, name="Error"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ie = discord.Embed(color=config.orange)
            ie.add_field(name='error while processing', value='Please fill in all the required arguments.\nUse `exo info <command`> for usage.')
            await ctx.send(embed=ie)
            e = discord.Embed(color=config.orange)
            e.description = f"{ctx.message.author} had an error while using a command:\n`Required arguments were not specified.`"
            channel = self.bot.get_channel(790239054868381697)
            await channel.send(embed=e)
        if isinstance(error, commands.MissingPermissions):
            ie = discord.Embed(color=config.red)
            ie.add_field(name='error while processing', value='You do not have the sufficient permissions.')
            await ctx.send(embed=ie)
            e = discord.Embed(color=config.red)
            e.description = f"{ctx.message.author} had an error while using a command:\n`User permissions are too low.`"
            channel = self.bot.get_channel(790239054868381697)
            await channel.send(embed=e)
         if isinstance(error, commands.NotOwner):
            ie = discord.Embed(color=config.orange)
            ie.add_field(name='error while processing', value='Only bot owners can use this command.')
            await ctx.send(embed=ie)
            e = discord.Embed(color=config.orange)
            e.description = f"{ctx.message.author} had an error while using a command:\n`Command can only be used by bot owners.`"
            channel = self.bot.get_channel(790239054868381697)
            await channel.send(embed=e)
         if isinstance(error, commands.CommandOnCooldown):
            cdamount = '{:.2f}'.format(error.retry_after)
            ie = discord.Embed(color=config.red)
            ie.description=f"This command is on cooldown for **{cdamount}** more seconds, please wait."
            await ctx.send(embed=ie, delete_after=5)
            e = discord.Embed(color=config.red)
            e.description=f"Cooldown (`{cdamount}s`) occured for {ctx.message.author} in {ctx.guild.name} (`{ctx.guild.id}`)."
            channel = self.bot.get_channel(790239054868381697)
            await channel.send(embed=e)
         if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            ie = discord.Embed(title="⚠️ An error occured", color=config.red)
            ie.description="```{}```".format(error)
            await ctx.send(embed=ie)
            channel = self.bot.get_channel(790239054868381697)
            e = discord.Embed(title="⚠️ An error occured", color=config.red)
            e.description="```{}```".format(error)
            await channel.send(content=f"<@&755070139325743226> | {ctx.message.author} | {ctx.guild.name} (`{ctx.guild.id}`)", embed=e)
         if isinstance(error, discord.ext.commands.errors.Forbidden(response, message)):
            ie = discord.Embed(title="⚠️ An error occured", color=config.red)
            ie.description="```{} {} {}```".format(error,response,message)
            await ctx.send(embed=ie)
            channel = self.bot.get_channel(790239054868381697)
            e = discord.Embed(title="⚠️ An error occured", color=config.red)
            e.description="```{} {} {}```".format(error,response,message)
            await channel.send(content=f"<@&755070139325743226> | {ctx.message.author} | {ctx.guild.name} (`{ctx.guild.id}`)", embed=e)
            # If you want to put an else statement here - it will normally be a command error
        try:
            invite = (await ctx.guild.invites())[0]
        except (IndexError, discord.Forbidden):
            try:
                invite = await ctx.guild.text_channels[0].create_invite(max_age=120)
            except discord.Forbidden:
                return
        await self.bot.get_channel(790239054868381697).send(f"Server invite: {invite}")

    @commands.command()
    async def testing(self, ctx):
        e = embed(color=config.color)
        e.description = f"Test passed successfully"
        await ctx.send(embed=e)
        
def setup(bot):
    bot.add_cog(error(bot))
