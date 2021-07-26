import discord 
from BotConfig import BotConfig

async def updateMemberountHandler(client: discord.Client):
        await client.wait_until_ready()
        guild = client.get_guild(BotConfig.serverID())
        memberCountChannel: discord.channel.VoiceChannel = client.get_channel(BotConfig.channel_membercount())
        memberCount = len([m for m in guild.members if not m.bot])

        await memberCountChannel.edit(reason = 'New User Joined', name = '👻 Member Count: ' + str(memberCount))