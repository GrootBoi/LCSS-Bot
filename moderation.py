import discord
import asyncio
import datetime
import json

from discord.ext import commands

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    def generalEmbedAction(self, member, reason, action):
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator + ' has been ' + action, icon_url = member.avatar_url)
        embed.add_field(name = 'For reason:', value = reason, inline = True)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed

    def generalEmbedActionNoReason(self, member, action):
        embed = self.generalEmbedAction(member, None, action)
        embed.remove_field(0)
        return embed

    def logsEmbedAction(self, ctx, member, reason, action):
        date = datetime.datetime.now()
        embed_logs = discord.Embed(color = 0xFFCB00)
        embed_logs.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed_logs.add_field(name = action, value = member.mention, inline = True)
        embed_logs.add_field(name = 'For reason:', value = reason, inline = True)
        embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed_logs

    def logsEmbedActionNoReason(self, ctx, member, action):
        embed_logs = self.logsEmbedAction(ctx, member, None, action)
        embed_logs.remove_field(1)
        return embed_logs

    def generalEmbedUnaction(self, member, action):
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator + ' has been ' + action, icon_url = member.avatar_url)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed

    def logsEmbedUnaction(self, ctx, member, action):
        date = datetime.datetime.now()
        embed_logs = discord.Embed(color = 0xFFCB00)
        embed_logs.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed_logs.add_field(name = action, value = member.mention, inline = True)
        embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        return embed_logs

    def logs(self):
        logs = self.client.get_channel(850777492297875467)
        return logs

    def role(self, ctx, name):
        role = discord.utils.get(ctx.guild.roles, name = name)
        return role

    async def permError(self, ctx, permission):
        await ctx.message.delete()
        await ctx.send(f'You are missing the {permission}', delete_after = 5.0)

    async def userError(self, ctx, format):
        await ctx.message.delete()
        await ctx.send(f'Please use this format: {format}', delete_after = 5.0)

#Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member: discord.Member, *, reason = None):
        await member.send('A parting gift from the Owner:\n⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪\n⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽')
        await member.ban(reason = reason)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'banned'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Banned'))

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Ban Members Permission')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!ban @User`')

#Softban
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def softban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await member.unban(reason = reason)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'soft banned'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Soft Banned'))

    @softban.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Ban Members Permission')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!softban @User`')

#Unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user: discord.User):
        await ctx.guild.unban(user)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedUnaction(user, 'unbanned'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, user, 'Unbanned'))
            
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Ban Members Permission')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!unban <@User ID (The 15/16 Digit One)>`')

#Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick (self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'kicked'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Kicked'))

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Kick Members Permission')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!kick @User`')

#Permanently Mute
    @commands.command()
    @commands.has_role('Staff')
    async def pmute(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'Muted'))
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'permanently muted'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Permanently Muted'))

    @pmute.error
    async def pmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!pmute @User`')

#Mute
    @commands.command()
    @commands.has_role('Staff')
    async def mute(self, ctx, member: discord.Member, duration, *, reason=None):
        await ctx.message.delete()
        #Getting Time for Mute
        number = duration[:-1]
        multiplier = duration[-1]
        if number.isnumeric():
            if self.role(ctx, 'Muted') not in member.roles:
                if int(number) > 0:
                    if multiplier == 's':
                        seconds = int(number)
                        time = 'second(s)'
                    elif multiplier == 'm':
                        seconds = int(number) * 60
                        time = 'minute(s)'
                    elif multiplier == 'h':
                        seconds = int(number) * 3600
                        time = 'hour(s)'
                    else:
                        await ctx.send('Invalid duration input')
        
                    embed = self.generalEmbedAction(member, reason, 'muted')
                    embed.insert_field_at(index = 0, name = 'Muted for Duration:', value = f'{number} {time}', inline = True)
                    embed_logs = self.logsEmbedAction(ctx, member, reason, 'Muted')
                    embed_logs.insert_field_at(index = 1, name = 'Muted for Duration:', value = f'{number} {time}', inline = True)

                    await member.add_roles(self.role(ctx, 'Muted'))
                    msg = await ctx.send(embed = embed)
                    await (self.logs()).send(embed = embed_logs)

                    asyncio.sleep(seconds)

                    await member.remove_roles(self.role(ctx, 'Muted'))
                    await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
                    await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))

                    #while self.role(ctx, 'Muted') in member.roles:
                        #if (datetime.datetime.utcnow() - msg.created_at) > datetime.timedelta(seconds = seconds):
                            #await member.remove_roles(self.role(ctx, 'Muted'))
                            #await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
                            #await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))

                else:
                    await ctx.send('Mute number must be greater than 0')
            else:
                await ctx.send('User is already muted!')
        else:
        	await ctx.send('Invalid duration input')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!mute @User (0h or 0m or 0s)`')
       
#Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def unmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'Muted'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!unmute @User`')
    
#Reaction Mute
    @commands.command()
    @commands.has_role('Staff')
    async def rmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete() 
        await member.add_roles(self.role(ctx, 'Reaction Muted'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'reaction muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Reaction Muted'))

    @rmute.error
    async def rmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!rmute @User`')

#Reaction Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def runmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'Reaction Muted'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'reaction unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Reaction Unmuted'))

    @runmute.error
    async def runmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!runmute @User`')

#Counting Mute
    @commands.command()
    @commands.has_role('Staff')
    async def cmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'YOU HAVE FAILED #counting'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'counting muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Counting Muted'))

    @cmute.error
    async def cmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!cmute @User`')

#Counting Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def cunmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'YOU HAVE FAILED #counting'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'counting unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Counting Unmuted'))

    @cunmute.error
    async def cunmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!cunmute @User`')

#Image and Embed Mute
    @commands.command()
    @commands.has_role('Staff')
    async def imute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'Image Banned'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'image/embed muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Image/Embed Muted'))

    @imute.error
    async def imute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!imute @User`')

#Image and Embed Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def iunmute(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'Image Banned'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'image/embed unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Image/Embed Unmuted'))

    @iunmute.error
    async def iunmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!iunmute @User`')
            
#Clear Messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number: int, *, member: discord.Member = None):
        await ctx.message.delete()
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        if member == None:
            await ctx.channel.purge(limit = number)
            embed_logs = discord.Embed(title = 'Bulk Messages Deleted', description = f'{number} messages cleared in {ctx.channel.mention}', color = 0xFFCB00)
            await ctx.send(f'{ctx.author} cleared {number} messages!', delete_after = 4.0)
            return

        else:
            await ctx.channel.trigger_typing()
            def is_user(message):
                return message.author == member
            message_counter = 0
            counter = 0
            async for m in ctx.channel.history(limit = None):
                message_counter += 1
                if m.author.id == member.id:
                    counter += 1
                    if counter == number:
                        await ctx.channel.purge(limit = message_counter, check = is_user)
                        embed_logs = discord.Embed(title = 'Bulk Messages Deleted', description = f'{number} messages cleared in {ctx.channel.mention} by {member.mention}', color = 0xFFCB00)
                        await ctx.send (f'{ctx.author} cleared {number} messages by {member.name}#{member.discriminator}!', delete_after = 4.0)
                        break

        embed_logs.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        await logs.send(embed = embed_logs)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Manage Messages Permission')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!clear (number)`')

#Slowmode
    @commands.command()
    @commands.has_role('Staff')
    async def slowmode(self, ctx, duration):
        await ctx.message.delete()

        embed = self.logsEmbedAction(ctx, None, None, 'Slowmode')
        embed.clear_fields()
        embed.insert_field_at(index = 0, name = 'In:', value = ctx.channel.mention)
        if duration.lower() == 'off':
            await ctx.channel.edit(slowmode_delay = 0)
            await ctx.send(f'Slow mode is now turned off. THE GHOSTS ARE FREE!!!! 👻')
            embed.insert_field_at(index = 0, name = 'Slowmode set to:', value = duration)
        else:
            await ctx.channel.edit(slowmode_delay = int(duration))
            await ctx.send(f'Slowmode has been set in this channel. Messages can only be sent once every {duration} seconds')
            embed.insert_field_at(index = 0, name = 'Slowmode set to:', value = duration + ' seconds')

        await (self.logs()).send(embed = embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!slowmode (seconds)')

#Warn
    @commands.command()
    @commands.has_role('Staff')
    async def warn(self, ctx, member: discord.Member, *, reason = None):
        await ctx.message.delete()
        #Opens Warn Files
        with open('warns.json', 'r') as f:
            data = json.load(f)
            if str(member.id) not in data:
                data[str(member.id)] = []
                data[str(member.id)].append({'warns': 0})
                with open('warns.json', 'w') as f:
                    json.dump(data, f, indent = 4)

            for num in data[str(member.id)]:
                warns = int(num['warns'])

            warns = (warns + 1)

            with open('warns.json', 'r') as f:
                data = json.load(f)
                data[str(member.id)] = []
                data[str(member.id)].append({'warns': warns})
                with open('warns.json', 'w') as f:
                    json.dump(data, f, indent = 4)
        #Logs Embed
        embed_logs = self.logsEmbedAction(ctx, member, reason, 'Warned')
        warnid = await (self.logs()).send(embed = embed_logs)
        embed_logs.insert_field_at(index = 2, name = 'Warn ID', value = warnid.id, inline = False)
        #General Embed
        embed = self.generalEmbedAction(member, reason, 'warned')
        embed.insert_field_at(index = 1, name = 'Warn ID', value = warnid.id, inline = False)

        await ctx.send(embed = embed)
        await warnid.edit(embed = embed_logs)
        #Automute for too much warnings
        if warns == 3:
            time = '1 hour'

        elif warns == 5:
            time = '3 hours'

        elif warns == 8:
            time = '12 hours'

        elif warns == 10:
            time = '24 hours'
        #General and Logs Embed
        embed = self.generalEmbedAction(member, f'Too many Warns ({warns})', 'muted')
        embed.insert_field_at(index = 0, name = 'Muted for Duration:', value = time, inline = True)
        embed_logs = self.logsEmbedAction(ctx, member, f'Too many Warns ({warns})', 'Muted')
        embed.insert_field_at(index = 1, name = 'Muted for Duration:', value = time, inline = True)

        async def multiplewarns(duration):
            await member.add_roles(self.role(ctx, 'Muted'))
            await ctx.send(embed = embed)
            await (self.logs()).send(embed = embed_logs)
            await asyncio.sleep(duration)
            await member.remove_roles(self.role(ctx, 'Muted'))
            await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
            await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))

        if warns == 3:
            await multiplewarns(3600)

        elif warns == 5:
            await multiplewarns(10800)

        elif warns == 8:
            await multiplewarns(43200)

        elif warns == 10:
            await multiplewarns(86400)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!warn @User')

#Remove Specific Warn
    @commands.command(aliases = ['warnremove'])
    @commands.has_role('Staff')
    async def removewarn(self, ctx, member: discord.Member, warnid):
        await ctx.message.delete()
        with open('warns.json', 'r') as f:
            data = json.load(f)
            if str(member.id) in data:
                for num in data[str(member.id)]:
                    warns = int(num['warns'])

                if warns > 0:
                    warns = (warns - 1)

                    with open('warns.json', 'r') as f:
                        data = json.load(f)
                        data[str(member.id)] = []
                        data[str(member.id)].append({'warns': warns,})
                        with open('warns.json', 'w') as f:
                            json.dump(data, f, indent = 4)

                    warnmessage: discord.Message = await (self.logs()).fetch_message(warnid)
                    await warnmessage.delete()
                    await ctx.send(f'Warn Removed!')
                
                elif warns == 0:
                    await ctx.send('User has no warns to be removed')
            else:
                await ctx.send('User has no warns to be removed')

    @removewarn.error
    async def removewarn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!removewarn @User (Warn ID)')

#Infractions
    @commands.command(aliases = ['warns'])
    @commands.has_role('Staff')
    async def infractions(self, ctx, member: discord.Member):
        await ctx.message.delete()
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator + ' Infractions', icon_url = member.avatar_url)
        with open('warns.json', 'r') as f:
            data = json.load(f)
            if str(member.id) in data:
                for num in data[str(member.id)]:
                    warns = int(num['warns'])
                    if warns > 0:
                        embed.add_field(name = '# of Infractions:', value = warns, inline = True)
                    elif warns == 0:
                        embed.add_field(name = '# of Infractions:', value = 'User has no infractions!', inline = True)
            else:
                embed.add_field(name = '# of Infractions:', value = 'User has no infractions!', inline = True)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        await ctx.send(embed = embed) 

    @infractions.error
    async def infractions_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await self.permError(ctx, 'Staff Role')
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '`!infractions @User')

def setup(client):
    client.add_cog(moderation(client))