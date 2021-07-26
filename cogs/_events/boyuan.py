import discord 
from BotConfig import BotConfig

async def shutUpBoyuan(channel: discord.TextChannel, member: discord.Member):
    try:
        if channel.guild.id == BotConfig.serverID():
            if member.id == 412316765918461955: #Boyuan's user id
                await channel.send(f'SHUT THE UP BOYUAN, DONT EVEN FINISH TYPING', delete_after = 8.0)
    except AttributeError:
        pass