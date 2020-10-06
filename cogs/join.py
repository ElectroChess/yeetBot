import discord
from discord.ext import commands
import random
import datetime

class join_leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id != 704482683857928222:
            return
        else:
            i=0
            for x in member.guild.members:
                if x.bot:
                    pass
                else:
                    i=i+1

            channel = self.bot.get_channel(731967941901549638)
            # if member.bot:
            # 	botchannel = self.bot.get_channel(704797031922663435)
            # 	await botchannel.send('botbotbo-ot-bo-')
            embed = discord.Embed(
                title='New member!',
                color=random.randint(0, 0xFFFFFF),
                timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(
                name=f"Thanks for joining {member.guild.name}, {member.name}!",
                value=f'We now have `{i}` members!')
            await channel.send(f'Welcome {member.mention} to **{member.guild.name}**', embed=embed)
            e2 = discord.Embed(
                description=
                'You dont have access to a lot of the channels because you arent verified yet. One of the staff members will verify you and you will get a dm when you are verified. Be patient.',
                color=random.randint(0, 0xffffff))
            await member.send(embed=e2)

def setup(bot):
    bot.add_cog(join_leave(bot))
