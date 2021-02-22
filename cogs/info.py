import discord, config, time, aiohttp, psutil, platform
from collections import Counter
from discord.ext import commands
from datetime import datetime
from utils import default

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
        e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)


    @commands.command(brief="Our privacy policy")
    async def privacy(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"""
You can read our privacy policy [here](https://github.com/ThePawKingdom/exorium/blob/master/privacy%20policy.md).
Want your data removed or got questions? mail to `bluewyechache@gmail.com`.
"""
        await ctx.send(embed=e)


    @commands.command(brief="Get support")
    async def support(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"""
You can get help in the following ways:
- Send a mail to `bluewyechache@gmail.com`
- [Join the support server](https://discord.gg/CEHkNky)
"""
        await ctx.send(embed=e)


    @commands.command(brief="exo related links")
    async def links(self, ctx):
        e = discord.Embed(color=config.color)
        e.description = f"""
- [statuspage](https://exorium.statuspage.io/)
Displays downtime, issues and outages.
- [bot lists](https://linktr.ee/exorium)
Links to all botlists exorium is on
- [GitHub repository](https://github.com/ThePawKingdom/exorium)
The open source code for exorium
"""
        await ctx.send(embed=e)


    @commands.command(brief="exorium statistics", aliases=["stats"])
    async def statistics(self, ctx):
        startTime = datetime.now().timestamp()
        print(startTime)
        print(datetime.now().timestamp())
        uptime = datetime.now().timestamp() - startTime
        channel_types = Counter(type(c) for c in self.bot.get_all_channels())
        voice = channel_types[discord.channel.VoiceChannel]
        text = channel_types[discord.channel.TextChannel]
        lastboot = str((datetime.utcfromtimestamp(uptime).strftime('%H hour(s), %M minute(s) and %S second(s)')))
        cpu_per = psutil.cpu_percent()
        cores = psutil.cpu_count()
        memory = psutil.virtual_memory().total >> 20
        mem_usage = psutil.virtual_memory().used >> 20
        storage_free = psutil.disk_usage('/').free >> 30
        e = discord.Embed(title="exorium statistics", color=config.color)
        e.description = f"""
__**About exorium**__
**Developers:** [Bluewy](https://discord.com/users/698080201158033409) & [Toothless](https://discord.com/users/341988909363757057)\n**Library:** [Discord.py {discord.__version__}](https://github.com/Rapptz/discord.py) <:python:758139554670313493>\n**Last boot:** {lastboot}
    
__**statistics**__
**guilds:** {str(len(self.bot.guilds))}\n**users:** {str(len(self.bot.users))}\n**channels:**\nText <:channel:719660740050419935> {text:,}\nVoice <:voice:719660766269145118> {voice:,}
__**System**__
**Hosting OS:** `{platform.platform()}`\n**Cores:** `{cores}`\n**CPU:** `{cpu_per}%`\n**RAM:** `{mem_usage}/{memory} MB`\n**Storage:** `{storage_free} GB free`
"""
        e.set_image(url=config.banner)
        await ctx.send(embed=e)
        

    @commands.command(brief="See a server's info", aliases=["si", "sinfo"])
    async def serverinfo(self, ctx):
        gu = ctx.guild
        features = ", ".join(gu.features).lower().replace('_', ' ').title()
        if len(features) == 0:
            features = None
        if gu.mfa_level == 0:
            mfa = "Optional"
        else:
            mfa = "Required"

        e = discord.Embed(color=config.color)
        e.add_field(name="__**Generic information**__",
                    value=f"**Owner:** {gu.owner}\n**Owner ID:**\n`{gu.owner.id}`\n**Created:** {default.date(ctx.guild.created_at)}\n**Region:** {str(gu.region)}\n**MFA: **{mfa}\n**Verification:** {str(ctx.guild.verification_level).capitalize()}", inline=True)
        e.add_field(name="__**Others**__",
                    value=f"**Humans:** {len(gu.bots)} ({len(gu.members)} total)\n**Bots:** {len(gu.humans)} ({len(gu.members)} total)\n**Text:** {len(gu.text_channels)} channels\n**Voice:** {len(gu.voice_channels)} channels", inline=True)
        if features != None:
            e.add_field(name="__**Server features**__", value=features, inline=False)
        e.set_author(name=f"{gu.name} information", icon_url=gu.icon_url)
        e.set_footer(text=f"Guild ID: {gu.id}")
        e.set_thumbnail(url=gu.icon_url)
        e.set_image(url=gu.banner_url)
        await ctx.send(embed=e)


    @commands.command(brief="See a user's info")
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.author
        roles = ''
        await ctx.send('test')
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            embed = discord.Embed(description=str(error), color=discord.Color.red())
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
