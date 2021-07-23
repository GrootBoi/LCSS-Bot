import discord
from BotConfig import BotConfig

async def _on_member_remove(client: discord.Client, member: discord.Member):
    guild = client.get_guild(BotConfig.serverID())
    welcomeChannel = client.get_channel(BotConfig.channel_welcome())
    membercountChannel = client.get_channel(BotConfig.channel_membercount())

    if member.guild.id == BotConfig.serverID():
        memberCount = len([m for m in guild.members if not m.bot])
        await membercountChannel.edit(reason = 'User Left', name = '👻 Member Count: ' + str(memberCount))

        embed = discord.Embed(
            title = 'Goodbye fellow Golden Ghost!', 
            description = 'Sorry to see you go!', 
            color = BotConfig.embedColor()
        )

        #Fix hardcoded icon url
        embed.set_author(
            name = f'{member.name}#{member.discriminator}', 
            icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg'
        )

        embed.set_thumbnail(url = member.avatar_url)
        
        await welcomeChannel.send(embed = embed)