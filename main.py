import discord
from discord.ext import commands
import os
import requests
import random
import asyncio


bot = commands.Bot(command_prefix=['y/', 'y.', '<@!757034804548993134> ', 'yeet '])
token = os.environ.get('token')
bot.remove_command('help')

def is_it_me(ctx):
	return ctx.author.id == 697535361315766322


@bot.event
async def on_ready():
	yeet = discord.utils.get(bot.guilds, id=704482683857928222)
	print('bot online!')
	snom = discord.utils.get(yeet.roles, id=723734065047666748)
	for x in yeet.members:
		if x.id == 538237760150962207:
			pass
		else:
			await x.remove_roles(snom)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
@commands.check(is_it_me)
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'Loaded {extension}')


@bot.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Unloaded {extension}')


@bot.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'Reloaded {extension}')

@bot.command()
async def test(ctx):
	i=0
	for x in ctx.guild.members:
		if x.bot:
			pass
		else:
			i=i+1
	print(i)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def verify(ctx, member: discord.Member):
	verifyRole = discord.utils.get(ctx.guild.roles, id=704809779918274560)
	await member.add_roles(verifyRole)
	embed = discord.Embed(
		description=f'Verified {member.mention}!', color=random.randint(0, 0xffffff))
	await ctx.send(embed=embed)

	e2 = discord.Embed(
		description=f'You were verified by {ctx.author.mention}',
		color=random.randint(0, 0xffffff))
	await member.send(embed=e2)

@bot.command(pass_context=True)
@commands.has_permissions(manage_emojis=True)
async def createEmoji(ctx, name, url):
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        return await ctx.send("The URL you have provided is invalid.")
    if response.status_code == 404:
        return await ctx.send("The URL you have provided leads to a 404.")
    try:
        emoji = await ctx.guild.create_custom_emoji(name=name, image=response.content)
    except discord.InvalidArgument:
        return await ctx.send("Invalid image type. Only PNG, JPEG and GIF are supported.")
    await ctx.send("Successfully added the emoji {0.name} <{1}:{0.name}:{0.id}>!".format(emoji, "a" if emoji.animated else ""))

bot.run(token)
