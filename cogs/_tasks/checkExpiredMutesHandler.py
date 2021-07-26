import discord
import datetime
from BotConfig import BotConfig
from jasper import db

async def checkExpiredMutesHandler(client: discord.Client):
    await client.wait_until_ready()
    guild = client.get_guild(BotConfig.serverID())
    punishmentChannel = client.get_channel(BotConfig.channel_punishment())

    muted = discord.utils.get(guild.roles, name = 'Muted')
    muteCollection = db["Mutes"]
    date = datetime.datetime.now()
    
    for muteRecord in muteCollection.find({}):
        member = await guild.fetch_member(int(muteRecord["_id"]))
        channel = client.get_channel(int(muteRecord["channel"]))

        if datetime.datetime.now() >= muteRecord["time"]:
            await member.remove_roles(muted)
            user = {"_id": member.id}
            muteCollection.delete_one(user)

            #Fix hardcoded icon url
            embed = discord.Embed(color = BotConfig.embedColor())
            embed.set_author(name = member.name + '#' + member.discriminator + ' has been unmuted', icon_url = member.avatar_url)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

            embed_logs = discord.Embed(color = BotConfig.embedColor())
            embed_logs.set_author(name = 'Jasper [BOT]', icon_url = client.user.avatar_url) #Fix hardcoded bot name
            embed_logs.add_field(name = 'Unmuted', value = member.mention, inline = True)
            embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

            await channel.send(embed = embed)
            await punishmentChannel.send(embed = embed_logs)