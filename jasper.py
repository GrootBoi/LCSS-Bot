import os
import discord
import asyncio
import datetime

from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
from BotConfig import BotConfig

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CONNECTION_URL = os.getenv('MONGODB_URL')

PREFIX = BotConfig.prefix()

intents = discord.Intents.all()
client = commands.Bot(
    command_prefix = PREFIX, 
    help_command = None, 
    intents = intents, 
    activity = discord.Activity(type = discord.ActivityType.watching, name = 'Over My Fellow Ghosts')
)

connection = MongoClient(CONNECTION_URL)
db = connection["Jasper"]

#Discord Bot Connection
@client.event
async def on_ready():
    date = datetime.datetime.now()
    print(f'{client.user.name} is connected at {date:%B %d, %Y} at {date:%H:%M} EST!')

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
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print('Load err')
            print(e)

#Loading Cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is loaded!', delete_after = 5.0)

@load.error
async def load_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send('Cog already loaded', delete_after = 3.0)

#Unloading Cogs
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is unloaded!', delete_after = 5.0)

@unload.error
async def unload_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send('Cog is not loaded', delete_after = 3.0)

#Refreshing Cogs
@client.command(aliases=['reload'])
@commands.is_owner()
async def refresh(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is refreshed!', delete_after = 5.0)

@refresh.error
async def refresh_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send('Cog is not loaded', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionFailed):
        await ctx.send('Cog refresh unsucessful, check command prompt. If nothing appears delete this error catch', delete_after = 3.0)
    
client.run(TOKEN)