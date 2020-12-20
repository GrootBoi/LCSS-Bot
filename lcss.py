import os
import asyncio
import random
import json
import discord

from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '`')

#Importing Initial Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Loading Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} cog is loaded!')

#Unloading Cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} cog is unloaded!')

#Refreshing Cogs
@client.command(aliases=['reload'])
async def refresh(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} cog is refreshed!')

#Member Joining
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the London Central Secondary School Discord!')
    print(f'{member.name} just joined the server!')

#Member Leaving
@client.event
async def on_member_remove(member):
    print(f'{member.name} just left the server :(')

#Check for the Shutdown Command
def isitme(ctx):
    return ctx.author.id == 524001661379936268

#!shutdown command
@client.command()
@commands.check(isitme)
async def shutdown(ctx):
    msg = await ctx.send (f'Shutting Down...')
    await ctx.message.delete() #Deletes User Command
    await asyncio.sleep(5)
    await msg.delete() #Deletes Bot Message
    await client.logout()
    print(f'\n{client.user} has disconnected from Discord!')

#!hsd command
@client.command()
@commands.check(isitme)
async def hsd(ctx):
    await ctx.message.delete()
    await ctx.send(f'{ctx.author} has performed a Hard Shut Down')
    await client.logout()
    print(f'\n{client.user} has disconnected from Discord!')

#Bot Status
@client.command(aliases=['green'])
async def online(ctx):
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(activity)))

@client.command(aliases=['yellow'])
async def idle(ctx):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(activity)))

@client.command(aliases=['donotdisturb', 'red'])
async def dnd(ctx):
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(activity)))
    
@client.command(aliases=['invisi', 'offline'])
async def invisible(ctx):
    await client.change_presence(status=discord.Status.invisible, activity=discord.Game(next(activity)))

#Discord Bot Connection
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Looking for Ghosts'))
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected to the following guild:\n'f'{guild.name}(ID: {guild.id})\n') #Kill
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    role = discord.utils.get(guild.roles, name = 'Staff') #Bot Commander Role Checker
    if not role:
        await guild.create_role(name = 'Staff', reason = 'To control/use the bot')
    else:
        return

#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Invalid Command')

client.run(TOKEN)
