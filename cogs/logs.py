import discord
import datetime

from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.raw_models import RawMessageDeleteEvent
from pytz import timezone

from BotConfig import BotConfig

class logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    def logsEmbed(self, action, author, name, value):
        date = datetime.datetime.now()
        embed = discord.Embed(title = action, color = BotConfig.embedColor())
        embed.set_author(name = author.name, icon_url = author.avatar_url)
        embed.add_field(name = name, value = value)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed

    def logsChannelEmbed(self, channel, action, staff):
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = str(channel.type).capitalize() + 'Channel ' + action, icon_url = channel.guild.icon_url)
        embed.add_field(name = 'Channel Name:', value = channel.mention + '\n' + channel.name)
        embed.add_field(name = action + ' By:', value = staff.user.mention)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed 

    def logs(self):
        logs = self.client.get_channel(BotConfig.channel_log())
        return logs
    
#User Join
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        timezone_convert_creation = member.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        if member.guild.id == BotConfig.serverID():
            await (self.logs()).send (embed = self.logsEmbed('Member Joined', member, 'Account Created:', creation))

#User Leave
    @commands.Cog.listener()
    async def on_member_leave(self, member: discord.Member):
        rolelist = [str(r.mention) for r in member.roles if r != member.guild.default_role]
        role = ", ".join(rolelist)
        if member.guild.id == BotConfig.serverID():
            await (self.logs()).send (embed = self.logsEmbed('Member Left', member, 'Roles:', role))

#Edited Messages
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        logs = self.client.get_channel(BotConfig.channel_log())
        if before.guild.id == BotConfig.serverID():
            date = datetime.datetime.now()
            embed = discord.Embed(title = 'Message Edited!', description = f'Message edited by: {before.author}', color = 0xFFCB00)
            embed.set_author(name = before.author, icon_url = before.author.avatar_url)
            if len(before.content) > 0  or len(after.content) > 0:
                embed.add_field(name = 'Before:', value = before.content)
                embed.add_field(name = 'Edited From:', value = before.channel.mention)
                embed.add_field(name = 'After:', value = after.content, inline = False)
            else:
                embed.add_field(name = 'Embed Edited From:', value = before.channel.mention)
            embed.add_field(name = 'Message Link:', value = f'https://discord.com/channels/700559773028057098/{before.channel.id}/{before.id}', inline = False)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await logs.send(embed = embed)

#Deleted Messages
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload: RawMessageDeleteEvent):
        logs = self.client.get_channel(BotConfig.channel_log())
        channel = self.client.get_channel(BotConfig.channel_botsetup())
        if payload.guild_id == BotConfig.serverID():
            date = datetime.datetime.now()
            embed = discord.Embed(title = 'Message Deleted!', description = f'Message by: {payload.cached_message.author}', color = BotConfig.embedColor())
            try:
                embed.set_author(name = payload.cached_message.author, icon_url = payload.cached_message.author.avatar_url)
                if len(payload.cached_message.content) > 0:
                    embed.add_field(name = 'Message Content:', value = payload.cached_message.content)
                    embed.add_field(name = 'Deleted From:', value = f'<#{payload.channel_id}>')
                else:
                    embed.add_field(name = 'Image/Embed Deleted From:', value = f'<#{payload.channel_id}>')
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
                await logs.send(embed = embed)
            except AttributeError:
                await channel.send('<@524001661379936268>')

#Bulk Deleted Messages
    @commands.Cog.listener()
    async def on_bulk_message_delete(self, payload):
        date = datetime.datetime.now()
        filelogs = open('C:\\Users\Flash123\Desktop\Jasper\BulkDeletes.txt', 'w')
        filelogs.write(f'Messages deleted at {date:%B %d, %Y} at {date:%H:%M} EST\n')
        filelogs.close()
        if payload[0].guild.id == BotConfig.serverID():
            for message in list(payload):
                filelogs = open('C:\\Users\Flash123\Desktop\Jasper\BulkDeletes.txt', 'a', encoding = 'utf-8')
                if len(message.content) > 0:
                    filelogs.write(f'Author: {message.author}, Channel: {message.channel}, Content: {message.content}\n')
                else:
                    filelogs.write(f'Author: {message.author}, Channel: {message.channel}, Image/Embed Deleted\n')
                filelogs.close()
            filelogs = open('C:\\Users\Flash123\Desktop\Jasper\BulkDeletes.txt', 'rb')
            filelogs.read()
            await (self.logs()).send(file = discord.File ('bulkdeletes.txt'))
            filelogs.close()

#Channel Created
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.guild.id == BotConfig.serverID():
            async for entry in channel.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_create):
                await (self.logs()).send(embed = self.logsChannelEmbed(channel, 'Created', entry))
        
#Channel Deleted
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.guild.id == BotConfig.serverID():
            async for entry in channel.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_delete):
                await (self.logs()).send(embed = self.logsChannelEmbed(channel, 'Deleted', entry))

#Channel Name Update
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.guild.id == BotConfig.serverID():
            async for entry in before.guild.audit_logs(limit = 1, action = discord.AuditLogAction.channel_update):
                if before.name != after.name:
                    embed = self.logsChannelEmbed(before, 'Edited', entry)
                    embed.insert_field_at(index = 2, name = 'New Channel Name:', value = after.name, inline = False)
                    await (self.logs()).send(embed = embed)

#Member Update
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == BotConfig.serverID():
            if len(before.roles) < len(after.roles):
                newRole = next(r for r in after.roles if r not in before.roles)
                await (self.logs()).send (embed = self.logsEmbed('Role Added', before, 'Added Role:', newRole.mention))
            elif len(before.roles) > len (after.roles):
                removedRole = next(r for r in before.roles if r not in after.roles)
                await (self.logs()).send (embed = self.logsEmbed('Role Removed', before, 'Removed Role:', removedRole.mention))
            elif before.nick != after.nick:
                embed = self.logsEmbed('Nickname Change', before, 'Old Nickname:', before.nick)
                embed.insert_field_at(index = 1, name = 'New Nickname:', value = after.nick)
                await (self.logs()).send(embed = embed)

#User Update
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        for guilds in before.mutual_guilds:
            if guilds.id == BotConfig.serverID():
                if before.name != after.name or before.discriminator != after.discriminator:
                    embed = self.logsEmbed('Username Change', before, 'Old Username:', before.name)
                    embed.insert_field_at(index = 1, name = 'New Username:', value = after.name)
                    await (self.logs()).send(embed = embed)

#Voice Channel Updates
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.guild.id == BotConfig.serverID():
            if not before.channel and after.channel:
                await (self.logs()).send(embed = self.logsEmbed('User Joined VC', member, 'Channel:', after.channel.mention))
            elif before.channel and not after.channel:
                await (self.logs()).send(embed = self.logsEmbed('User Left VC', member, 'Channel:', before.channel.mention))
            elif before.channel != None and after.channel != None:
                if before.self_mute == False and after.self_mute == True:
                    await (self.logs()).send(embed = self.logsEmbed('User Muted Themself', member, 'Channel:', after.channel.mention))
                elif before.self_mute == True and after.self_mute == False:
                    await (self.logs()).send(embed = self.logsEmbed('User Unmuted Themself', member, 'Channel:', after.channel.mention))
                elif before.self_stream == False and after.self_stream == True:
                    await (self.logs()).send(embed = self.logsEmbed('User Started Streaming', member, 'Channel:', after.channel.mention))
                elif before.self_stream == True and after.self_stream == False:
                    await (self.logs()).send(embed = self.logsEmbed('User Stopped Streaming', member, 'Channel:', after.channel.mention))
                elif before.self_video == False and after.self_video == True:
                    await (self.logs()).send(embed = self.logsEmbed('User Turned Their Camera On', member, 'Channel:', after.channel.mention))
                elif before.self_video == True and after.self_video == False:
                    await (self.logs()).send(embed = self.logsEmbed('User Turned Their Camera Off', member, 'Channel:', after.channel.mention))
                elif before.mute == False and after.mute == True:
                    embed = self.logsEmbed('User Muted in VC', member, 'Channel:', after.channel.mention)
                    async for entry in member.guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.insert_field_at(index = 1, name = 'Muted By:', value = entry.user.mention)
                        await (self.logs()).send(embed = embed)
                elif before.mute == True and after.mute == False:
                    embed = self.logsEmbed('User Unmuted in VC', member, 'Channel:', after.channel.mention)
                    async for entry in member.guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.insert_field_at(index = 1, name = 'Unmuted By:', value = entry.user.mention)
                        await (self.logs()).send(embed = embed)
                elif before.deaf == False and after.deaf == True:
                    embed = self.logsEmbed('User Deafened in VC', member, 'Channel:', after.channel.mention)
                    async for entry in member.guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.insert_field_at(index = 1, name = 'Deafened By:', value = entry.user.mention)
                        await (self.logs()).send(embed = embed)
                elif before.deaf == True and after.deaf == False:
                    embed = self.logsEmbed('User Undeafened in VC', member, 'Channel:', after.channel.mention)
                    async for entry in member.guild.audit_logs(limit = 1, action = discord.AuditLogAction.member_update):
                        embed.insert_field_at(index = 1, name = 'Undeafened By:', value = entry.user.mention)
                        await (self.logs()).send(embed = embed)
            elif not before.requested_to_speak_at and after.requested_to_speak_at:
                await (self.logs()).send(embed = self.logsEmbed('User Requested to Speak', member, 'Channel:', before.channel.mention))
            elif before.requested_to_speak_at and not after.requested_to_speak_at:
                await (self.logs()).send(embed = self.logsEmbed('User Accepted/Declined to Speak', member, 'Channel:', before.channel.mention))
            elif not before.suppress and after.suppress:
                await (self.logs()).send(embed = self.logsEmbed('User is Speaking', member, 'Channel:', before.channel.mention))
            elif before.suppress and not after.suppress:
                await (self.logs()).send(embed = self.logsEmbed('User Stopped Speaking', member, 'Channel:', before.channel.mention))

def setup(client):
    client.add_cog(logs(client))