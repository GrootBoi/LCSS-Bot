import discord
import datetime

from discord.ext import commands
from pytz import timezone

class info(commands.Cog):

    def __init__ (self, client):
        self.client = client

    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787

#Owner
    @commands.command()
    async def owner(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'The Owner', description = f'The owner of this server is {ctx.guild.owner.mention}', color = 0xFFCB00)
        await ctx.send(embed = embed)

#Bot Info
    @commands.command()
    async def botinfo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'About Me!', description = 'The bot is coded with Python. The owner of the bot is <@524001661379936268>', color = 0xFFCB00)
        await ctx.send(embed = embed)

#Staff
    @commands.command(aliases = ['mods', 'mod'])
    async def staff(self, ctx):
        await ctx.message.delete()
        guild = self.client.get_guild(700559773028057098)
        admin = guild.get_role(700934813757997108)
        adminlist = [str(m.mention) for m in admin.members]
        admins = ", ".join(adminlist)
        moderator = guild.get_role(700561779595542578)
        moderatorlist = [str(m.mention) for m in moderator.members]
        moderators = ", ".join(moderatorlist)
        embed = discord.Embed(title = 'Staff Members', description = 'Meet our Staff Members!', color = 0xFFCB00)
        embed.add_field(name = 'Owner', value = guild.owner.mention, inline = True)
        embed.add_field(name = f'Admins ({len(adminlist)})', value = admins, inline = False)
        embed.add_field(name = f'Moderators ({len(moderatorlist)})', value = moderators, inline= False)
        await ctx.send(embed = embed)

#Covid Information
    @commands.command()
    async def covid(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'COVID Cases', description = "Unfortunately I can't do that yet, look to the Daily Info Category or type `c/stats` to find out information about COVID Cases.\nFor School Status type !ss\n\nAlternatively, you can use the links below:", color = 0xFFCB00)
        embed.add_field(name = 'London:', value = 'https://www.healthunit.com/covid-19-cases-middlesex-london', inline = False)
        embed.add_field(name = 'Ontario:', value = 'https://covid-19.ontario.ca/covid-19-epidemiologic-summaries-public-health-ontario', inline = False)
        embed.set_footer(text = "In the case that you don't believe COVID is real, you may 'polietly' go fuck yourself")
        await ctx.send(embed = embed)

#School Status
    @commands.command(aliases = ['ss'])
    async def schoolstatus(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Ontario Schools Status', description = 'As of April 12th 2021, all Ontario Schools will be closed until further notice', color = 0xFFCB00)
        await ctx.send(embed = embed)

#Invite Link
    @commands.command()
    async def invite(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Permanent Invite Link:', description = 'https://discord.gg/26jGM68MCA', color = 0xFFCB00)
        await ctx.send(embed = embed)

#Avatar
    @commands.command(aliases = ['av'])
    async def avatar(self, ctx, *, member: commands.MemberConverter = None):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator)
        embed.set_image(url = member.avatar_url)
        await ctx.send(embed = embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!av @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#User Info
    @commands.command(aliases = ['user'])
    async def userinfo(self, ctx, *, member: commands.MemberConverter = None):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        rolelist = [str(r.mention) for r in member.roles if r != ctx.guild.default_role]
        role = ", ".join(rolelist)
        timezone_convert_creation = member.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        timezone_convert_join = member.joined_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        joined = timezone_convert_join.strftime('%B %d, %Y at %H:%M EST')
        if member.raw_status == 'online':
            status = '🟢 Online'
        elif member.raw_status == 'idle':
            status = '🟡 Idle'
        elif member.raw_status == 'dnd':
            status = '🔴 Do not Disturb/DND'
        elif member.raw_status == 'offline':
            status = '⚫ Offline/Invisible'
        else:
            status = '🟣 Streaming'
        embed = discord.Embed(title = f'User Info For: {member.name}#{member.discriminator}', color = 0xFFCB00)
        embed.set_thumbnail(url = member.avatar_url)
        embed.add_field(name = 'Bio:', value = member.activity, inline = False)
        embed.add_field(name = 'Account Created:', value = creation)
        embed.add_field(name = 'Joined Server:', value = joined)
        embed.add_field(name = 'Status:', value = status)
        embed.add_field(name = f'Roles ({len(rolelist)}):', value = role, inline = False)
        await ctx.send(embed = embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!av @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#Server Info
    @commands.command(aliases = ['server'])
    async def serverinfo(self, ctx):
        await ctx.message.delete()
        allmembers = ctx.guild.member_count
        members = len([m for m in ctx.guild.members if not m.bot])
        bots = allmembers - members
        roles = [str(r.mention) for r in ctx.guild.roles]
        allchannels = [str(c) for c in ctx.guild.channels]
        categories = [str(c) for c in ctx.guild.categories]
        channels = [str(c) for c in ctx.guild.text_channels]
        vc = [str(c) for c in ctx.guild.voice_channels]
        emotes = [str(e) for e in ctx.guild.emojis]
        timezone_convert_creation = ctx.guild.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        embed = discord.Embed(title = 'Server Info For: ' + ctx.guild.name, color = 0xFFCB00)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.add_field(name = 'Owner:', value = ctx.guild.owner.mention)
        embed.add_field(name = 'Server Created:', value = creation)
        embed.add_field(name = '\u200b', value = '\u200b')
        embed.add_field(name = 'Roles:', value = f'{len(roles)}\n(!roles to get list)')
        embed.add_field(name = 'Emotes:', value = f'{len(emotes)}\n(!emotes to get list)')
        embed.add_field(name = 'Members:', value = f'Total Members: {allmembers}\nMembers: {members}, Bots: {bots}')
        embed.add_field(name = 'Channels:', value = f'Total Channels: {len(allchannels)}, Catergories: {len(categories)}, Text Channels: {len(channels)}, Voice Channels: {len(vc)}')
        await ctx.send(embed = embed)

#Role Info
    @commands.command(aliases = ['role'])
    async def roleinfo(self, ctx, *, role: commands.RoleConverter):
        await ctx.message.delete()
        if str(role.colour) == '#000000':
            color = 0xFCCB00
        else:
            color = role.colour
        memberlist = [str(m.mention) for m in role.members]
        timezone_convert_creation = role.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        embed = discord.Embed(title = 'Role Info For: ' + role.name, color = color)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.add_field(name = 'Role Created:', value = creation, inline = False)
        embed.add_field(name = 'ID', value = f'`{role.id}`')
        embed.add_field(name = 'Mentionable?', value = role.mentionable)
        embed.add_field(name = '# of Members:', value = len(memberlist))
        embed.set_footer(text = 'Use !rolelist to get a list of users with a role')
        await ctx.send(embed = embed)

    @roleinfo.error
    async def roleinfo_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!roleinfo (Role)`', delete_after = 5.0)
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send('Please send a valid role', delete_after = 5.0)

#Role with list of members
    @commands.command()
    async def rolelist(self, ctx, *, role: commands.RoleConverter):
        await ctx.message.delete()
        memberlist = [str(m.mention) for m in role.members]
        members = " ".join(memberlist)
        embed = discord.Embed(title = f'Members in {role.name} ({len(memberlist)}):', description = members, color = 0xFCCB00)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed = embed)

    @rolelist.error
    async def rolelist_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!rolelist (Role)`', delete_after = 5.0)
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send('Please send a valid role', delete_after = 5.0)

#List of all roles
    @commands.command()
    async def roles(self, ctx):
        await ctx.message.delete()
        rolelist = [str(r.mention) for r in ctx.guild.roles if r != ctx.guild.default_role]
        role = " ".join(rolelist)
        embed = discord.Embed(title = 'Roles List:', description = role, color = 0xFCCB00)
        embed.set_footer(text = 'You might be looking for the !roleinfo command instead')
        await ctx.send(embed = embed)

#Emotes list
    @commands.command()
    async def emotes(self, ctx):
        await ctx.message.delete()
        emotelist = [str(e) for e in ctx.guild.emojis]
        emotes = " ".join(emotelist)
        embed = discord.Embed(title = 'Emotes List:', description = emotes, color = 0xFCCB00)
        await ctx.send(embed = embed)

#Leafs last cup
    @commands.command()
    async def leafs(self, ctx):
        await ctx.message.delete()
        today = datetime.datetime.today()
        lastcup = datetime.datetime.strptime('05-02-1967', '%m-%d-%Y')
        threeone = datetime.datetime.strptime('05-31-2021', '%m-%d-%Y')
        serieswin = datetime.datetime.strptime('04-20-2004', '%m-%d-%Y')
        zamboni = datetime.datetime.strptime('02-22-2020', '%m-%d-%Y')
        cupdrought = datetime.datetime.strptime('07-03-2021', '%m-%d-%Y')
        lastcupdays = (today - lastcup).days
        threeonedays = (today - threeone).days
        serieswindays = (today - serieswin).days
        zambonidays = (today - zamboni).days
        cupdroughtdays = (today - cupdrought).days
        embed = discord.Embed(title = 'Leafs Stats!', description = "Welcome to the shitshow of the Toronto Maple Leafs! Here are some FUN STATS\nHere's some info to catch you up!\nhttps://www.youtube.com/watch?v=25j6s-ZY3mY", color = 0x00205B)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/818494514867077144/849804790511042560/pandaleafs.png')
        embed.add_field(name = f'{lastcupdays} days since winning a Cup', value = 'Last Cup Win: May 2nd, 1967', inline = False)
        embed.add_field(name = f'{threeonedays} days since blowing a 3-1 playoff lead to the Montreal Canadiens', value = 'Blew Series Lead On: May 31st, 2021', inline = False)
        embed.add_field(name = f'{serieswindays} days since winning a playoff series', value = 'Last Series Win: April 20, 2004', inline = False)
        embed.add_field(name = f'{zambonidays} days since losing to a 42 YEAR OLD ZAMBONI DRIVER THAT WORKS FOR YOUR MINOR LEAGUE AFFILIATE', value = 'Date Lost: April 22nd, 2020\nSteve Dangle: https://www.youtube.com/watch?v=QFnQ0dcaBUI', inline = False)
        embed.add_field(name = f'{cupdroughtdays} days since the Leafs have set the record for the longest Stanley Cup drought in NHL History', value = 'Date Set: July 4, 2021', inline = False)
        embed.set_footer(text = '#LeafsForever', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/849808217667665950/5a4fbbd0da2b4f099b95da1f.png')
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(info(client))