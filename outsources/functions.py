import discord
import config
import random
import gifs
from outsources import util


async def interactions(ctx, members, reason, type, ending, typespecial):
    GIFlist = getattr(gifs, type)
    GIF = random.choice(GIFlist)
    if not (members):
        return await ctx.send(f"Please specify at least one cutie to {type}!")
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + f"**{typespecial}**" + " " + '**,** '.join(x.mention for x in members) + f"**, {ending}!**\nFor: " + reason))
    embed.set_footer(text="Check info about the gifs/images with exo help social, and help us!")
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


# async def logging(ctx, type, bot):
#     print(f"Command \"{type}\" was used in {ctx.channel} (guild {ctx.guild}) by {ctx.message.author}")
#     embed = discord.Embed(title="exorium command log", color=config.color)
#     embed.add_field(name="Command", value=f"`\"{type}\"`", inline=True)
#     embed.add_field(name="Author", value=f"`{ctx.message.author}`", inline=True)
#     embed.add_field(name="Guild", value=f"`{ctx.guild}`", inline=True)
#     embed.add_field(name="Channel", value=f"`{ctx.channel}`", inline=True)
#     channel = bot.get_channel(755138117488345118)
#     await channel.send(embed=embed)

async def logging(ctx, type, bot):
    print(f"\"{type}\" used in {ctx.channel} | {ctx.guild} by {ctx.message.author}")
    e = discord.Embed(color=config.color)
    
    mcreated = f"{ctx.message.created_at.strftime('%d.%m.%Y %H:%M')}"
    createday = ctx.message.author.created_at.weekday()
    ucreated = f"{util.weekdays[createday]} {ctx.message.author.created_at.strftime('%d.%m.%Y %H:%M')}"
    
    e.description = f"""
__**Command info**__
**Command:** `{type}`
**Message ID:** [{ctx.message.id}]({ctx.message.jump_url}) (Click to go to message)
**Message date:** {mcreated}

__**User info**__
**Username:** {ctx.message.author} | **ID:** `{ctx.message.author.id}`
**Created at:** {ucreated}

__**Guild info**__
**Guild name:** {ctx.guild.name} | **guild ID:** {ctx.guild.id}
**Owner name:** [{ctx.guild.owner}](https://discord.com/users/{ctx.guild.owner_id})
"""
    channel = bot.get_channel(755138117488345118)
    await channel.send(embed=e)
