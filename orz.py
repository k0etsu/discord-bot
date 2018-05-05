import discord
import discord.ext
import asyncio
from discord.ext import commands
import random
import logging
import re

logging.basicConfig(level=logging.INFO)

botDescription = '''orz'''

bot = commands.Bot(command_prefix='!', description=botDescription)

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------------')

@bot.command()
async def add(left: int, right: int):
  """Adds two numbers together. Duh. Idiot."""
  await bot.say(left + right)

@bot.command()
async def roll(dice: str):
  """Roll dice mofo - NdN format"""
  try:
    rolls, limit = map(int, dice.split('d'))
  except Exception:
    await bot.say('Format must be NdN')
    return

  result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
  await bot.say(result)

@bot.command(pass_context=True)
async def color(ctx, hex: str):
  """Change your role color. For when you're lazy."""

  hex = hex.replace("#","")
  x = int(hex, 16)
  server_id = ctx.message.server.id
  user = ctx.message.author
  new_color = discord.Colour(x)
  role = discord.utils.get(ctx.message.server.roles, name=user.name)

  if role != None:
    await bot.delete_role(discord.Object(server_id), role)

  new_role = await bot.create_role(discord.Object(server_id), name=user.name, colour=new_color)
  await bot.add_roles(user,new_role)

@bot.command()
async def status(status: str):
  """Changes the bot's status"""

  new_status = discord.Game()
  new_status.name = status
  await bot.change_status(new_status, idle=False)


bot.run()
