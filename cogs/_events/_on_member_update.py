from BotConfig import BotConfig
import discord

async def _on_member_update(client: discord.Client, before: discord.Member, after: discord.Member):
    guild = client.get_guild(BotConfig.serverID())
    member = guild.get_member(before.id)
    rolePleaseIdentify = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')

    identifiedRoles = map(
        lambda roleName: discord.utils.get(guild.roles, name = roleName), 
        ['Alumni', 'Grade 12', 'Grade 11', 'Grade 10', 'Other Schools']
    )

    for identifiedRole in identifiedRoles:
        try:
            if rolePleaseIdentify in before.roles and after.roles:
                if identifiedRole not in before.roles and identifiedRole in after.roles:
                    await member.remove_roles(rolePleaseIdentify, reason = 'User Identified Themself')
        except AttributeError:
            return