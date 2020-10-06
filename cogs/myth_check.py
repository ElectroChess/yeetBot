import discord
from discord.ext import commands

class myth_check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        mythify = discord.utils.get(after.guild.roles, id=760595871296389250)
        if after.id == 475315771086602241:
            return
        else:
            if mythify in after.roles:
                await after.remove_roles(mythify)
            else:
                pass

def setup(bot):
    bot.add_cog(myth_check(bot))
