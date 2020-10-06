import discord
from discord.ext import commands

class mutedChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not before.channel and after.channel:
            role = discord.utils.get(
                member.guild.roles, name="Currently in a voice channel")
            await member.add_roles(role)
        elif before.channel and not after.channel:
            role = discord.utils.get(
                member.guild.roles, name="Currently in a voice channel")
            await member.remove_roles(role)

def setup(bot):
    bot.add_cog(mutedChat(bot))