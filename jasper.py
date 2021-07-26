from Utils import Utils
import os
import discord
import asyncio

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

#!shutdown command
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    msg = await ctx.send (f'Shutting Down...')
    await asyncio.sleep(3)
    await msg.delete()
    await client.close()
    Utils.log_info(f'\n{client.user} has disconnected from Discord!')

#!hsd command
@client.command()
@commands.is_owner()
async def hsd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = 'A Hard Shut Down has been performed', color = BotConfig.embedColor())
    await ctx.send(embed = embed)
    await client.close()

    Utils.log_info(f'\n{client.user} has disconnected from Discord!')

#Load all cogs on start up
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
            Utils.log_info(f'Loading cog {filename}')
        except Exception as e:
            Utils.log_error(f'Error with loading cog {filename}\n{e}')

#Load a cog after client instantiated 
@client.command()
@commands.is_owner()
async def load(ctx: commands.Context, extension: str):
    client.load_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is loaded!', delete_after = 5.0)

@load.error
async def load_error(ctx: commands.Context, error: Exception):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send('Cog already loaded', delete_after = 3.0)

#Unload a cog after client instantiated
@client.command()
@commands.is_owner()
async def unload(ctx: commands.Context, extension: str):
    client.unload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is unloaded!', delete_after = 5.0)

@unload.error
async def unload_error(ctx: commands.Context, error: Exception):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send('Cog is not loaded', delete_after = 3.0)

#Refreshing a cog after client instantiated
@client.command(aliases=['reload'])
@commands.is_owner()
async def refresh(ctx: commands.Context, extension: str):
    client.reload_extension(f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'The {extension} cog is refreshed!', delete_after = 5.0)

@refresh.error
async def refresh_error(ctx: commands.Context, error: Exception):
    await ctx.message.delete()
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Cog not found', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send('Cog is not loaded', delete_after = 3.0)
    elif isinstance(error, commands.ExtensionFailed):
        await ctx.send('Cog refresh unsucessful, check command prompt. If nothing appears delete this error catch', delete_after = 3.0)
    
client.run(TOKEN)