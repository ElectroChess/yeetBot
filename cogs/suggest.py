import discord
import random
from discord.ext import commands


class suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx):
        MSGe = await ctx.send('What image do you want to suggest')

        def check(m):
            return m.author.id == ctx.author.id

        response = await self.bot.wait_for('message', check=check)
        await MSGe.edit(content='Sent! Go check out <#707062922337189939>')
        icon_suggest = self.bot.get_channel(707062922337189939)
        embed = discord.Embed(title='New icon suggest', color=ctx.author.color)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=response.attachments[0].url)
        msg = await icon_suggest.send(embed=embed)
        await msg.add_reaction('<:upvote:729048211649462282>')
        await msg.add_reaction('<:downvote:729048490784849931>')


def setup(bot):
    bot.add_cog(suggest(bot))
