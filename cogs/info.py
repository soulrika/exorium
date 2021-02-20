import discord, config, time, aiohttp
from discord.ext import commands

class info(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(brief="Bot's latency to discord")
    async def ping(self, ctx):
        """ See bot's latency to discord """
        discord_start = time.monotonic()
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com') as r:
                if r.status == 200:
                    discord_end = time.monotonic()
                    discord_ms = f"{round((discord_end - discord_start) * 1000)}ms"
                else:
                    discord_ms = "fucking dead"
                await ctx.send(f"\U0001f3d3 Pong   |   {discord_ms}")# You can use :ping_pong: instead of \U0001f3d3

    
    @commands.command(brief="The invites for exorium")
    async def invite(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"""
[needed permissions (recommended)](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=335932630&scope=bot)
- Only has the permissions the bot needs
[admin permissions (not recommended](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=8&scope=bot)
- Has the admin permission alone
[no permissions](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=0&scope=bot)
- Zero permissions (bot may not work well)
"""
        await ctx.send(embed=e)
        

    @commands.command(brief="test command")
    async def respond(self, ctx, *, args):
        e = discord.Embed(color=config.color)
        e.description = f"{args}"
        e.set_footer(text=f"by {ctx.message.author}")
        await ctx.send(embed=e)


    @commands.command(brief="Our privacy policy")
    async def privacy(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"""
You can read our privacy policy [here](https://github.com/ThePawKingdom/exorium/blob/master/privacy%20policy.md).
Want your data removed or got questions? Send an email to `bluewyechache@gmail.com`.
"""
        await ctx.send(embed=e)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            embed = discord.Embed(description=str(error), color=discord.Color.red())
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
