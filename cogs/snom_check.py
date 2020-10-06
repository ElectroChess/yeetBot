import discord
from discord.ext import commands

class snom_check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        snom = discord.utils.get(after.guild.roles, id=723734065047666748)
        if after.id == 538237760150962207:
            return
        else:
            if snom in after.roles:
                await after.remove_roles(snom)
            else:
                pass
            

def setup(bot):
    bot.add_cog(snom_check(bot))
