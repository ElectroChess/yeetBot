import discord
import random
import datetime
from discord.ext import commands


class helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title='YeetBot Commands',
            description='Developed by <@!697535361315766322>',
            color=random.randint(0, 0xffffff),
            timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(
            url=
            'https://cdn.discordapp.com/avatars/757034804548993134/434a9986ebe5b4ae7b2476275c64220d.webp?size=1024'
        )
        embed.add_field(
            name='Make a Public Announcement',
            value='`y.announce`',
            inline=False)
        embed.add_field(name='Suggest an Icon', value='`y.suggest`', inline=False)
        embed.set_footer(
            text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(helpcmd(bot))
