import discord
from discord.ext import commands
import random
import datetime
class join_leave(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = self.bot.get_channel(731967941901549638)
		if member.bot:
			botchannel = self.bot.get_channel(704797031922663435)
			await botchannel.send('')
		# else:	
		# 	e = discord.Embed(title = 'New Member!', color = 0xffff00)
		# 	e.add_field(f'Member Name: {member.name}')
		# 	e.set_icon
		# 	await channel.send()

def setup(bot):
	bot.add_cog(join_leave(bot))
