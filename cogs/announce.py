import discord
import random
from discord.ext import commands


class announce(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 300, commands.BucketType.user)
	async def announce(self, ctx):
		channel = self.bot.get_channel(704810410456383649)
		await ctx.send('What would you like to announce?')

		def check(m):
			return m.author.id == ctx.author.id

		response = await self.bot.wait_for('message', check=check)
		response = str(response.content)

		await ctx.send(
			'Would you like to include an image? (if yes send one) (if no say no)'
		)

		image = await self.bot.wait_for('message', check=check)
		if str(image.content).lower() == 'no':
			embed = discord.Embed(
			title='Public Announcement',
			description=response,
			color=random.randint(0, 0xffffff))
			embed.set_author(
			name=ctx.author, icon_url=ctx.author.avatar_url)
			await channel.send('<@&723279578268696648>', embed=embed)

		else:			
			url = image.attachments[0].url		
			embed = discord.Embed(
			title='Public Announcement',
			description=response,
			color=random.randint(0, 0xffffff))
			embed.set_author(
			name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.set_image(url=url)	
			await channel.send('<@&723279578268696648>', embed=embed)
			

	@announce.error
	async def announce_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			msg = f'You are on cooldown\nTry Again in `{round(int(error.retry_after))}` seconds'
			await ctx.send(msg)


def setup(bot):
	bot.add_cog(announce(bot))
