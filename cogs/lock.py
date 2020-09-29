import discord
import random
from discord.ext import commands


class lockdown(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def lockServer(self, ctx):
		online_role = discord.utils.get(ctx.guild.roles, id=704809779918274560)
		channels = ctx.guild.text_channels
		for x in channels:
			if '🦢・' in str(x):
				await x.set_permissions(online_role, send_messages=False, read_messages=True, read_message_history=True)
		await ctx.send('Locked')
	
	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def unlockServer(self, ctx):
		online_role = discord.utils.get(ctx.guild.roles, id=704809779918274560)
		channels = ctx.guild.text_channels		
		for x in channels:
			if'🦢・' in str(x):
                await x.set_permissions(online_role, send_messages=True, read_messages=True, create_instant_invite=True, embed_links=True, attach_files=True, read_message_history=True, use_external_emojis=True, add_reactions=True)#pls stop#uut ok
				
		await ctx.send('Un-Locked!')






def setup(bot):
	bot.add_cog(lockdown(bot))
