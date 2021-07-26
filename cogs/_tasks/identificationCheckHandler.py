import discord 
import datetime

from BotConfig import BotConfig
from Utils import Utils

async def identificationCheckHandler(client: discord.Client):
    await client.wait_until_ready()

    raiseException = False
    guild: discord.Guild = client.get_guild(BotConfig.serverID())
    rolePleaseIdentify: discord.Role = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')
    identifiedRoles: map[discord.Role] = map(
        lambda roleName: discord.utils.get(guild.roles, name = roleName), 
        ['Alumni', 'Grade 12', 'Grade 11', 'Grade 10', 'Other Schools']
    )

    guildMembers: list[discord.Member] = guild.members

    for member in guildMembers:
        identified = False

        for identifiedRole in identifiedRoles:
            if identifiedRole in member.roles:
                identified = True
                break

        if not identified and (datetime.datetime.utcnow() - member.joined_at) > datetime.timedelta(hours = 4):
            try:
                await member.add_roles(rolePleaseIdentify)
            except Exception as e: 
                #Failed to add role (likely due to insuffecient perms), warn to console once
                if not raiseException:
                    Utils.log_warning(f'Failed to add identification role during the identification task\n{e}')
                    raiseException = True