import discord
from BotConfig import BotConfig

async def welcomeHandler(client: discord.Client, member: discord.Member):
    guild = client.get_guild(BotConfig.serverID())
    welcomeChannel = client.get_channel(BotConfig.channel_welcome())
    generalChannel = client.get_channel(BotConfig.channel_general())
    membercountChannel = client.get_channel(BotConfig.channel_membercount())

    if member.guild.id == BotConfig.serverID():

        #Fix hardcoded channel ids later
        embed = discord.Embed(
            title = 'Welcome fellow Golden Ghost!', 
            description = 'Please read <#700571972362567763> and enjoy your stay!\nAlso stop by <#700563120690561024> to get identified!', 
            color = BotConfig.embedColor()
        )
        
        #Fix hardcoded icon url later
        embed.set_author(
            name = f'{member.name}#{member.discriminator}', 
            icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg'
        )

        embed.set_thumbnail(url = member.avatar_url)

        await welcomeChannel.send(embed = embed)

        memberCount = len([m for m in guild.members if not m.bot])
        await membercountChannel.edit(reason = 'New User', name = '👻 Member Count: ' + str(memberCount))

        try:
            await member.send("Hello Golden Ghost, I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")
        except discord.HTTPException:
            #Fix hardcoded channel id
            await generalChannel.send(f"Hello {member.mention}! Since your DMs have been turned off, I'll do my little speech here. I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")