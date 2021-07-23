import discord
import asyncio
import datetime

from discord.ext import commands
from jasper import db

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    muted = db["Mutes"]
    warned = db["Warns"]

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

#Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member: commands.MemberConverter, *, reason = None):
        await ctx.message.delete()
        try:
            await member.send('A parting gift from the Owner:\n⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪\n⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽')
        except discord.HTTPException:
            pass
        await member.ban(reason = reason)
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'banned'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Banned'))

    @ban.error
    async def ban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the Ban Members Permission', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!ban @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Softban
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def softban(self, ctx, member: commands.MemberConverter, *, reason = None):
        await ctx.message.delete()
        await member.ban(reason = reason)
        await member.unban(reason = reason)
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'soft banned'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Soft Banned'))

    @softban.error
    async def softban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the Ban Members Permission', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!softban @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user: commands.UserConverter):
        await ctx.guild.unban(user)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedUnaction(user, 'unbanned'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, user, 'Unbanned'))
            
    @unban.error
    async def unban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the Ban Members Permission', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!unban @User`', delete_after = 5.0)
        elif isinstance(error, commands.UserNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick (self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason = reason)
        await ctx.message.delete()
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'kicked'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Kicked'))

    @kick.error
    async def kick_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the Kick Members Permission', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!kick @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Permanently Mute
    @commands.command()
    @commands.has_role('Staff')
    async def pmute(self, ctx, member: commands.MemberConverter, *, reason=None):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'Muted'))
        try:
            await member.send('While you are muted, the Owner wished to send you this:\n⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪\n⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽')
        except discord.HTTPException:
            pass
        await ctx.send(embed = self.generalEmbedAction(member, reason, 'permanently muted'))
        await (self.logs()).send(embed = self.logsEmbedAction(ctx, member, reason, 'Permanently Muted'))

    @pmute.error
    async def pmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!pmute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Mute
    @commands.command()
    @commands.has_role('Staff')
    async def mute(self, ctx, member: commands.MemberConverter, duration, *, reason=None):
        await ctx.message.delete()
        #Getting Time for Mute
        number = duration[:-1]
        unit = duration[-1]
        if number.isnumeric():
            if self.role(ctx, 'Muted') not in member.roles:
                if int(number) > 0:
                    multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
                    value = {'s': ' second(s)', 'm': ' minute(s)', 'h': ' hour(s)', 'd': ' day(s)'}
                    seconds = int(number) * multiplier[unit]
        
                    embed = self.generalEmbedAction(member, reason, 'muted')
                    embed.insert_field_at(index = 0, name = 'Muted for Duration:', value = number + value[unit], inline = True)
                    embed_logs = self.logsEmbedAction(ctx, member, reason, 'Muted')
                    embed_logs.insert_field_at(index = 1, name = 'Muted for Duration:', value = number + value[unit], inline = True)

                    await member.add_roles(self.role(ctx, 'Muted'))
                    try:
                        await member.send('While you are muted, the Owner wished to send you this:\n⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪\n⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽')
                    except discord.HTTPException:
                        pass
                    await ctx.send(embed = embed)
                    await (self.logs()).send(embed = embed_logs)

                    if seconds <= 300:
                        await asyncio.sleep(seconds)
                        await member.remove_roles(self.role(ctx, 'Muted'))
                        await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
                        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))
                    else:
                        unmute_time = datetime.datetime.now() + datetime.timedelta(seconds = seconds)
                        mutectx = {"_id": member.id, "channel": ctx.channel.id, "time": unmute_time}
                        self.muted.insert_one(mutectx)
                else:
                    await ctx.send('Mute number must be greater than 0', delete_after = 4.0)
            else:
                await ctx.send('User is already muted!', delete_after = 4.0)
        else:
        	await ctx.send('Invalid duration input', delete_after = 4.0)

    @mute.error
    async def mute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!mute @User (0d or 0h or 0m or 0s)`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)
       
#Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def unmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        user = {"_id": member.id}
        self.muted.delete_one(user)
        await member.remove_roles(self.role(ctx, 'Muted'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Unmuted'))

    @unmute.error
    async def unmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!unmute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)
    
#Reaction Mute
    @commands.command()
    @commands.has_role('Staff')
    async def rmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete() 
        await member.add_roles(self.role(ctx, 'Reaction Muted'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'reaction muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Reaction Muted'))

    @rmute.error
    async def rmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!rmute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Reaction Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def runmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'Reaction Muted'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'reaction unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Reaction Unmuted'))

    @runmute.error
    async def runmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!rumute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Counting Mute
    @commands.command()
    @commands.has_role('Staff')
    async def cmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'YOU HAVE FAILED #counting'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'counting muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Counting Muted'))

    @cmute.error
    async def cmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!cmute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Counting Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def cunmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'YOU HAVE FAILED #counting'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'counting unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Counting Unmuted'))

    @cunmute.error
    async def cunmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!cumute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Image and Embed Mute
    @commands.command()
    @commands.has_role('Staff')
    async def imute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        await member.add_roles(self.role(ctx, 'Image Banned'))
        await ctx.send(embed = self.generalEmbedActionNoReason(member, 'image/embed muted'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Image/Embed Muted'))

    @imute.error
    async def imute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!imute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Image and Embed Unmute
    @commands.command()
    @commands.has_role('Staff')
    async def iunmute(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        await member.remove_roles(self.role(ctx, 'Image Banned'))
        await ctx.send(embed = self.generalEmbedUnaction(member, 'image/embed unmuted'))
        await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Image/Embed Unmuted'))

    @iunmute.error
    async def iunmute_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!iumute @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)
            
#Clear Messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number: int, *, member: commands.MemberConverter = None):
        await ctx.message.delete()
        logs = self.client.get_channel(831327025394483240)
        date = datetime.datetime.now()
        if number > 0:
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

        else:
            await ctx.send('Number of messages cleared must be greater than 0')

    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the Manage Messages Permission', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!clear (Number) (*@User) *Not mandatory`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Slowmode
    @commands.command()
    @commands.has_role('Staff')
    async def slowmode(self, ctx, duration):
        await ctx.message.delete()
        date = datetime.datetime.now()
        if duration.isnumeric() or duration.lower() == 'off':
            embed_logs = discord.Embed(color = 0xFFCB00)
            embed_logs.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed_logs.add_field(name = 'In:', value = ctx.channel.mention)
            if duration.lower() == 'off':
                await ctx.channel.edit(slowmode_delay = 0)
                await ctx.send('Slow mode is now turned off. THE GHOSTS ARE FREE!!!! 👻')
                embed_logs.add_field(name = 'Slowmode set to:', value = duration)
            else:
                await ctx.channel.edit(slowmode_delay = int(duration))
                await ctx.send(f'Slowmode has been set in this channel. Messages can only be sent once every {duration} seconds')
                embed_logs.add_field(name = 'Slowmode set to:', value = duration + ' seconds')
            embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            if duration.lower() == 'off' and ctx.channel.slowmode_delay == 0 or int(duration) < 1:
                if ctx.channel.slowmode_delay == 0:
                    await ctx.send('Slowmode is already off', delete_after = 4.0)
                else:
                    await ctx.send('Slowmode duration must be greater than 0', delete_after = 4.0)
            else:
                await (self.logs()).send(embed = embed_logs)
        else:
            await ctx.send('Invalid Value Given')

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!slowmode (Number)`', delete_after = 5.0)

#Warn
    @commands.command()
    @commands.has_role('Staff')
    async def warn(self, ctx, member: commands.MemberConverter, *, reason = None):
        await ctx.message.delete()
        user = {"_id": member.id}
        if (self.warned.count_documents(user) == 0):
            warns = 1
            warnctx = {"_id": member.id, "warns": warns, f"reason#{warns}": reason}
            self.warned.insert_one(warnctx)
        else:
            for x in self.warned.find(user):
                warns = x["warns"]
            warns += 1
            self.warned.update_one({"_id": member.id}, {"$set":{"warns":warns}})

        await ctx.send(embed = self.generalEmbedAction(member, reason, 'warned'))
        await (self.logs()).send(embed = self.logsEmbedActionNoReason(ctx, member, 'Warned'))

        if warns >= 3: 
            #Automute for too much warnings
            if warns == 3:
                hours = 1
            elif warns == 5:
                hours = 3
            elif warns == 8:
                hours = 12
            elif warns == 10:
                hours = 24

            #General and Logs Embed
            embed = self.generalEmbedAction(member, f'Too many Warns ({warns})', 'muted')
            embed.insert_field_at(index = 0, name = 'Muted for Duration:', value = f'{hours} hour(s)', inline = True)
            embed_logs = self.logsEmbedAction(ctx, member, f'Too many Warns ({warns})', 'Muted')
            embed.insert_field_at(index = 1, name = 'Muted for Duration:', value = f'{hours} hour(s)', inline = True)

            await member.add_roles(self.role(ctx, 'Muted'))
            await ctx.send(embed = embed)
            await (self.logs()).send(embed = embed_logs)

            unmute_time = datetime.datetime.now() + datetime.timedelta(hours = hours)
            mutectx = {"_id": member.id, "channel": ctx.channel.id, "time": unmute_time}
            self.muted.insert_one(mutectx)

    @warn.error
    async def warn_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!warn @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Remove Specific Warn
    @commands.command(aliases = ['warnremove', 'rwarn'])
    @commands.has_role('Staff')
    async def removewarn(self, ctx, member: commands.MemberConverter):
        await ctx.message.delete()
        user = {"_id": member.id}
        if (self.warned.count_documents(user) == 0):
            await ctx.send('User has no warns to be removed', delete_after = 4.0)
        else:
            for x in self.warned.find(user):
                warns = x["warns"]
            if warns == 0:
                await ctx.send('User has no warns to be removed', delete_after = 4.0)
            else:
                warns -= 1
                self.warned.update_one({"_id": member.id}, {"$set":{"warns":warns}})
                user = {"_id": ctx.author.id}
                await ctx.send(embed = self.generalEmbedUnaction(member, 'warn removed'))
                await (self.logs()).send(embed = self.logsEmbedUnaction(ctx, member, 'Removed Warn'))
                await ctx.send(f'Warn Removed!')

    @removewarn.error
    async def removewarn_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!removewarn @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Infractions
    @commands.command(aliases = ['warns'])
    @commands.has_role('Staff')
    async def infractions(self, ctx, member: commands.MemberConverter):
        await ctx.message.delete()
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator + ' Infractions', icon_url = member.avatar_url)
        user = {"_id": member.id}
        if (self.warned.count_documents(user) == 0):
            embed.add_field(name = '# of Infractions:', value = 'User has no infractions!', inline = True)
        else:
            for x in self.warned.find(user):
                warns = x["warns"]
            if warns == 0:
                embed.add_field(name = '# of Infractions:', value = 'User has no infractions!', inline = True)
            else:
                embed.add_field(name = '# of Infractions:', value = warns, inline = True)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        await ctx.send(embed = embed) 

    @infractions.error
    async def infractions_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the Staff Role', delete_after = 5.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use this format: `!infractions @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

def setup(client):
    client.add_cog(moderation(client))