import discord
from discord.ext import commands
import os
import keep_alive
import random
bot = commands.Bot(command_prefix=['y/', 'y.', '<@!757034804548993134> ', 'yeet '])
token = os.environ.get('token')
bot.remove_command('help')

def is_it_me(ctx):
  return ctx.author.id == 697535361315766322


@bot.event
async def on_ready():
    print('bot online!')

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


keep_alive.keep_alive()
bot.run(token)
