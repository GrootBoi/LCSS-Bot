import discord
import datetime

from discord.ext import commands
from pytz import timezone

class logs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #User Join
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        date = datetime.datetime.now()
        logs = self.client.get_channel(831327025394483240)
        timezone_convert_creation = member.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = member.created_at.strftime('%B %d, %Y at %H:%M UTC')
        if member.guild.id == 700559773028057098:
            embed = discord.Embed(title = 'Member Joined!', color = 0xFFCB00)
            embed.set_author(name = member.name, icon_url = member.avatar_url)
            embed.add_field(name = 'Account Created:', value = f'{creation}', inline = False)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await logs.send(embed = embed)

    #User Leave
    @commands.Cog.listener()
    async def on_member_leave(self, member: discord.Member):
        date = datetime.datetime.now()
        logs = self.client.get_channel(831327025394483240)
        rolelist = [str(r.mention) for r in member.roles if r != member.guild.default_role]
        role = ", ".join(rolelist)
        if member.guild.id == 700559773028057098:
            embed = discord.Embed(title = 'Member Left!', color = 0xFFCB00)
            embed.set_author(name = member.name, icon_url = member.avatar_url)
            embed.add_field(name = 'Roles:', value = f'{role}', inline = False)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await logs.send(embed = embed)

    #Edited Messages
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        logs = self.client.get_channel(831327025394483240)
        if message_before.guild.id == 700559773028057098:
            date = datetime.datetime.now()
            embed = discord.Embed(title = 'Message Edited!', description = f'Message edited by: {message_before.author}', color = 0xFFCB00)
            embed.set_author(name = message_before.author, icon_url = message_before.author.avatar_url)
            if len(message_before.content) > 0  or len(message_after.content) > 0:
                embed.add_field(name = 'Before:', value = message_before.content)
                embed.add_field(name = 'Edited From:', value = f'<#{message_before.channel.id}>')
                embed.add_field(name = 'After:', value = message_after.content, inline = False)
            else:
                embed.add_field(name = 'Embed Edited From:', value = f'<#{message_before.channel.id}>')
            embed.add_field(name = 'Message Link:', value = f'https://discord.com/channels/700559773028057098/{message_before.channel.id}/{message_before.id}', inline = False)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await logs.send(embed = embed)

    #Deleted Messages
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        logs = self.client.get_channel(831327025394483240)
        if payload.guild_id == 700559773028057098:
            date = datetime.datetime.now()
            embed = discord.Embed(title = 'Message Deleted!', description = f'Message by: {payload.cached_message.author}', color = 0xFFCB00)
            embed.set_author(name = payload.cached_message.author, icon_url = payload.cached_message.author.avatar_url)
            if len(payload.cached_message.content) > 0:
                embed.add_field(name = 'Message Content:', value = payload.cached_message.content)
                embed.add_field(name = 'Deleted From:', value = f'<#{payload.channel_id}>')
            else:
                embed.add_field(name = 'Image/Embed Deleted From:', value = f'<#{payload.channel_id}>')
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await logs.send(embed = embed)

    #Bulk Deleted Messages
    @commands.Cog.listener()
    async def on_bulk_message_delete(self, payload):
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        filelogs = open('C:\\Users\Flash123\Desktop\LCSS_bot\BulkDeletes.txt', 'w')
        filelogs.write(f'Messages deleted at {date:%B %d, %Y} at {date:%H:%M} EST\n')
        filelogs.close()
        if payload[0].guild.id == 700559773028057098:
            for message in list(payload):
                filelogs = open('C:\\Users\Flash123\Desktop\LCSS_bot\BulkDeletes.txt', 'a', encoding = 'utf-8')
                if len(message.content) > 0:
                    filelogs.write(f'Author: {message.author}, Channel: {message.channel}, Content: {message.content}\n')
                else:
                    filelogs.write(f'Author: {message.author}, Channel: {message.channel}, Image/Embed Deleted\n')
                filelogs.close()
            filelogs = open('C:\\Users\Flash123\Desktop\LCSS_bot\BulkDeletes.txt', 'rb')
            filelogs.read()
            await logs.send(file = discord.File ('bulkdeletes.txt'))
            filelogs.close()

    #Channel Created
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        date = datetime.datetime.now()
        guild = self.client.get_guild(700559773028057098)
        logs = self.client.get_channel(831327025394483240)
        if channel.guild.id == 700559773028057098:
            async for entry in channel.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_create):
                embed = discord.Embed(color = 0xFFCB00)
                embed.set_author(name = f'{str(channel.type).capitalize()} Channel Created!', icon_url = guild.icon_url)
                embed.add_field(name = 'Channel Name:', value = channel.mention + '\n' + channel.name)
                embed.add_field(name = 'Created By:', value = entry.user.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)

    #Channel Deleted
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        date = datetime.datetime.now()
        guild = self.client.get_guild(700559773028057098)
        logs = self.client.get_channel(831327025394483240)
        if channel.guild.id == 700559773028057098:
            async for entry in channel.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_delete):
                embed = discord.Embed(color = 0xFFCB00)
                embed.set_author(name = f'{str(channel.type).capitalize()} Channel Deleted!', icon_url = guild.icon_url)
                embed.add_field(name = 'Channel Name:', value = channel.name)
                embed.add_field(name = 'Deleted By:', value = entry.user.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)

    #Channel Name Update
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        guild = self.client.get_guild(700559773028057098)
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        if before.guild.id == 700559773028057098:
            async for entry in before.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_update):
                if before.name != after.name:
                    embed = discord.Embed(color = 0xFFCB00)
                    embed.set_author(name = f'{str(before.type).capitalize()} Channel Name Update!', icon_url = guild.icon_url)
                    embed.add_field(name = 'Old Channel Name:', value = before.name)
                    embed.add_field(name = 'Deleted By:', value = entry.user.mention)
                    embed.add_field(name = 'New Channel Name:', value = after.name, inline = False)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)

    #Member Update
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        if before.guild.id == 700559773028057098:
            if len(before.roles) < len(after.roles):
                newRole = next(r for r in after.roles if r not in before.roles)
                embed = discord.Embed(title = 'Role Added!', color = 0xFFCB00)
                embed.set_author(name = before.name, icon_url = before.avatar_url)
                embed.add_field(name = f'Added Role:', value = newRole.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif len(before.roles) > len (after.roles):
                removedRole = next(r for r in before.roles if r not in after.roles)
                embed = discord.Embed(title = 'Role Removed!', color = 0xFFCB00)
                embed.set_author(name = before.name, icon_url = before.avatar_url)
                embed.add_field(name = f'Removed Roles:', value = removedRole.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif before.nick != after.nick:
                embed = discord.Embed(title = 'Nickname Change!', color = 0xFFCB00)
                embed.set_author(name = before.name, icon_url = before.avatar_url)
                embed.add_field(name = 'Old Nickname:', value = before.nick)
                embed.add_field(name = 'New Nickname:', value = after.nick)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)

    #User Update
    @commands.Cog.listener()
    async def on_user_update(self, member_before, member_after):
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        for guilds in member_before.mutual_guilds:
            if guilds.id == 700559773028057098:
                if member_before.name != member_after.name or member_before.discriminator != member_after.discriminator:
                    embed = discord.Embed(title = 'Username Change!', color = 0xFFCB00)
                    embed.set_author(name = member_before.name, icon_url = member_before.avatar_url)
                    embed.add_field(name = 'Old Nickname:', value = member_before.name)
                    embed.add_field(name = 'New Nickname:', value = member_after.name)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)

    #Voice Channel Updates
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = self.client.get_guild(700559773028057098)
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        if member.guild.id == 700559773028057098:
            if not before.channel and after.channel:
                embed = discord.Embed(title = 'User Joined VC!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = after.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif before.channel and not after.channel:
                embed = discord.Embed(title = 'User Left VC!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = before.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif before.channel != None and after.channel != None:
                if before.self_mute == False and after.self_mute == True:
                    embed = discord.Embed(title = 'User Muted Themself!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.self_mute == True and after.self_mute == False:
                    embed = discord.Embed(title = 'User Unmuted Themself!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.self_stream == False and after.self_stream == True:
                    embed = discord.Embed(title = 'User Started Streaming!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.self_stream == True and after.self_stream == False:
                    embed = discord.Embed(title = 'User Stopped Streaming!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.self_video == False and after.self_video == True:
                    embed = discord.Embed(title = 'User Has Turned Their Camera On!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.self_video == True and after.self_video == False:
                    embed = discord.Embed(title = 'User Has Turned Their Camera Off!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                    await logs.send(embed = embed)
                elif before.mute == False and after.mute == True:
                    embed = discord.Embed(title = 'User Muted in VC!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    async for entry in guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.add_field(name = 'Muted By:', value = entry.user.mention)
                        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                        await logs.send(embed = embed)
                elif before.mute == True and after.mute == False:
                    embed = discord.Embed(title = 'User Unmuted in VC!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    async for entry in guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.add_field(name = 'Unmuted By:', value = entry.user.mention)
                        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                        await logs.send(embed = embed)
                elif before.deaf == False and after.deaf == True:
                    embed = discord.Embed(title = 'User Deafened in VC!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    async for entry in guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.add_field(name = 'Deafened By:', value = entry.user.mention)
                        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                        await logs.send(embed = embed)
                elif before.deaf == True and after.deaf == False:
                    embed = discord.Embed(title = 'User Undeafened in VC!', color = 0xFFCB00)
                    embed.set_author(name = member.name, icon_url = member.avatar_url)
                    embed.add_field(name = 'Channel:', value = after.channel.mention)
                    async for entry in guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.add_field(name = 'Undeafened By:', value = entry.user.mention)
                        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                        await logs.send(embed = embed)
            elif not before.requested_to_speak_at and after.requested_to_speak_at:
                embed = discord.Embed(title = 'User Requested to Speak!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = before.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif before.requested_to_speak_at and not after.requested_to_speak_at:
                embed = discord.Embed(title = 'User has been Accepted/Declined to Speak!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = before.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif not before.suppress and after.suppress:
                embed = discord.Embed(title = 'User is Speaking!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = before.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            elif before.suppress and not after.suppress:
                embed = discord.Embed(title = 'User has Stopped Speaking!', color = 0xFFCB00)
                embed.set_author(name = member.name, icon_url = member.avatar_url)
                embed.add_field(name = 'Channel:', value = before.channel.mention)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)

def setup(client):
    client.add_cog(logs(client))