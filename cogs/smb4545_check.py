import discord
from discord.ext import commands

class smb4545_check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        smbrole = discord.utils.get(after.guild.roles, id=760941046694674514)
        if after.id == 697913907528073296:
            return
        else:
            if smbrole in after.roles:
                await after.remove_roles(smbrole)
            else:
                pass

def setup(bot):
    bot.add_cog(smb4545_check(bot))
