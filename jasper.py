import os
import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CONNECTION_URL = os.getenv('MONGODB_URL')

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', help_command = None, intents = intents)

connection = MongoClient(CONNECTION_URL)
db = connection["Jasper"]

#Discord Bot Connection
@client.event
async def on_ready():
    guild = client.get_guild(700559773028057098)
    vc = client.get_channel(734139663903752292)
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'Events Unfold, Hate has no place anywhere'))
    print(f'The {client.user.name} is connected!')
    members = len([m for m in guild.members if not m.bot])
    await vc.edit(reason = 'New User', name = '👻 Member Count: ' + str(members))

#!shutdown command
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    msg = await ctx.send (f'Shutting Down...')
    await asyncio.sleep(3)
    await msg.delete()
    await client.close()
    print(f'\n{client.user} has disconnected from Discord!')

#!hsd command
@client.command()
@commands.is_owner()
async def hsd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = 'A Hard Shut Down has been performed', color = 0xFFCB00)
    await ctx.send(embed = embed)
    await client.close()
    print(f'\n{client.user} has disconnected from Discord!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Loading Cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is loaded!', delete_after = 5.0)

#Unloading Cogs
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is unloaded!', delete_after = 5.0)

#Refreshing Cogs
@client.command(aliases=['reload'])
@commands.is_owner()
async def refresh(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is refreshed!', delete_after = 5.0)
    
client.run(TOKEN)