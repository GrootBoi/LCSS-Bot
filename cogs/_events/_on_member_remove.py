import discord

async def _on_member_remove(client: discord.Client, member: discord.Member, GUILD_ID: int, WELCOME_CHANNEL_ID: int, MEMBERCOUNT_CHANNEL_ID: int):
    guild = client.get_guild(GUILD_ID)
    welcomeChannel = client.get_channel(WELCOME_CHANNEL_ID)
    membercountChannel = client.get_channel(MEMBERCOUNT_CHANNEL_ID)

    if member.guild.id == GUILD_ID:
        members = len([m for m in guild.members if not m.bot])
        await membercountChannel.edit(reason = 'User Left', name = '👻 Member Count: ' + str(members))

        embed = discord.Embed(
            title = 'Goodbye fellow Golden Ghost!', 
            description = 'Sorry to see you go!', 
            color = 0xFFCB00
        )

        #Fix hardcoded icon url
        embed.set_author(
            name = f'{member.name}#{member.discriminator}', 
            icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg'
        )

        embed.set_thumbnail(url = member.avatar_url)
        await welcomeChannel.send(embed = embed)