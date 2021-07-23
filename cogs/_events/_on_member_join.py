import discord

#wew, a long of params... this will be fixed later down the line as a single object containing bot config
async def _on_member_join(client: discord.Client, member: discord.Member, 
GUILD_ID: int, WELCOME_CHANNEL_ID: int, GENERAL_CHANNEL_ID: int, MEMBERCOUNT_CHANNEL_ID: int):
    guild = client.get_guild(GUILD_ID)
    welcomeChannel = client.get_channel(WELCOME_CHANNEL_ID)
    generalChannel = client.get_channel(GENERAL_CHANNEL_ID)
    membercountChannel = client.get_channel(MEMBERCOUNT_CHANNEL_ID)


    if member.guild.id == GUILD_ID:

        #Fix hardcoded channel ids later
        embed = discord.Embed(
            title = 'Welcome fellow Golden Ghost!', 
            description = 'Please read <#700571972362567763> and enjoy your stay!\nAlso stop by <#700563120690561024> to get identified!', 
            color = 0xFFCB00
        )
        
        #Fix hardcoded icon url later
        embed.set_author(
            name = f'{member.name}#{member.discriminator}', 
            icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg'
        )

        embed.set_thumbnail(url = member.avatar_url)

        await welcomeChannel.send(embed = embed)

        members = len([m for m in guild.members if not m.bot])
        await membercountChannel.edit(reason = 'New User', name = '👻 Member Count: ' + str(members))

        try:
            await member.send("Hello Golden Ghost, I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")
        except discord.HTTPException:

            #Fix hardcoded channel id
            await generalChannel.send(f"Hello {member.mention}! Since your DMs have been turned off, I'll do my little speech here. I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")