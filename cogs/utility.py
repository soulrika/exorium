import discord, config, json, requests, random
from discord.ext import commands

class utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Get someone's ID")
    async def id(self, ctx, member: discord.Member):
        await ctx.send(member.id)

    
    @commands.command(brief="generate random animals")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def animal(self, ctx, *args):
        delmsg = await ctx.send('Awaiting api results')
        query = ''
        for thing in args:
            query += f"{thing}+"
        if query.endswith('+'):
            query = query[:-1]
        else:
            query = "animal"
        r = requests.get(
            'https://pixabay.com/api/',
            params={'key': config.pixabaykey, 'q': query, "image_type": 'photo', 'category': 'animals'}
        )
        if r.json()["total"] == 0:
            await delmsg.delete()
            await ctx.send("Sadly, no results were found")
            return
        await delmsg.delete()
        finalimg = random.choice(r.json()["hits"])["webformatURL"]
        embed = discord.Embed(title='Random animal', color=config.color)
        embed.set_image(url=finalimg)
        embed.set_footer(text='Powered by pixabay.')
        await ctx.send(embed=embed)


    @commands.command(brief="Generate random images")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def image(self, ctx, *args):
        delmsg = await ctx.send('Awaiting api results')
        query = ''
        for thing in args:
            query += f"{thing}+"
        if query.endswith('+'):
            query = query[:-1]
        else:
            query = "animal"
        r = requests.get(
            'https://pixabay.com/api/',
            params={'key': config.pixabaykey, 'q': query, "image_type": 'photo', 'safesearch': 'true'}
        )
        if r.json()["total"] == 0:
            await delmsg.delete()
            await ctx.send("Sadly, no results were found")
            return
        await delmsg.delete()
        finalimg = random.choice(r.json()["hits"])["webformatURL"]
        embed = discord.Embed(title='Random animal', color=config.color)
        embed.set_image(url=finalimg)
        embed.set_footer(text='Powered by pixabay.')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utility(bot))
