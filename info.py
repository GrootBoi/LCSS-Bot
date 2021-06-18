import discord
import datetime
import asyncio

from discord.ext import commands
from datetime import date
from pytz import timezone

class info(commands.Cog):

    def __init__ (self, client):
        self.client = client

    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787

    #!owner
    @commands.command()
    async def owner(self, ctx):
        guild = self.client.get_guild(700559773028057098)
        embed = discord.Embed(title = 'The Owner', description = f'The owner of this server is {guild.owner.mention}', color = 0xFFCB00)
        await ctx.send(embed = embed)
        await ctx.message.delete()        

    #!botinfo
    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title = 'About Me!', description = 'The bot is coded with Python. The owner of the bot is <@524001661379936268>', color = 0xFFCB00)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #!staff
    @commands.command(aliases = ['mods', 'mod'])
    async def staff(self, ctx):
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
        await ctx.message.delete()

    #!covid
    @commands.command()
    async def covid(self, ctx):
        embed = discord.Embed(title = 'COVID Cases', description = "Unfortunately I can't do that yet, look to the Daily Info Category or type `c/stats` to find out information about COVID Cases.\nFor School Status type !ss\n\nAlternatively, you can use the links below:", color = 0xFFCB00)
        embed.add_field(name = 'London:', value = 'https://www.healthunit.com/covid-19-cases-middlesex-london', inline = False)
        embed.add_field(name = 'Ontario:', value = 'https://covid-19.ontario.ca/covid-19-epidemiologic-summaries-public-health-ontario', inline = False)
        embed.set_footer(text = "In the case that you don't believe COVID is real, you may 'polietly' go fuck yourself")
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #!schoolstatus
    @commands.command(aliases = ['ss'])
    async def schoolstatus(self, ctx):
        embed = discord.Embed(title = 'Ontario Schools Status', description = 'As of April 12th 2021, all Ontario Schools will be closed until further notice', color = 0xFFCB00)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #!invite
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title = 'Permanent Invite Link:', description = 'https://discord.gg/26jGM68MCA', color = 0xFFCB00)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #avatar
    @commands.command(aliases = ['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator)
        embed.set_image(url = member.avatar_url)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            avatar_error = await ctx.send(f'Please mention the user with the command')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await avatar_error.delete()

    #userinfo
    @commands.command(aliases = ['user'])
    async def userinfo(self, ctx, *, member: discord.Member = None):
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
        activity = member.activity
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator, icon_url = member.avatar_url)
        embed.add_field(name = 'Activity:', value = f'{activity}', inline = True)
        embed.add_field(name = 'Status:', value = f'{status}', inline = True)
        embed.add_field(name = 'Account Created:', value = f'{creation}', inline = False)
        embed.add_field(name = 'Joined Server:', value = f'{joined}', inline = False)
        embed.add_field(name = f'Roles ({len(rolelist)}):', value = f'{role}', inline = False)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            userinfo_error = await ctx.send(f'Please mention the user with the command')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await userinfo_error.delete()

    #serverinfo
    @commands.command(aliases = ['server'])
    async def serverinfo(self, ctx):
        guild = self.client.get_guild(700559773028057098)
        date = datetime.datetime.now()
        owner = guild.owner
        allmembers = guild.member_count
        members = len([m for m in guild.members if not m.bot])
        bots = allmembers - members
        roles = [str(r.mention) for r in ctx.guild.roles]
        allchannels = [str(c) for c in ctx.guild.channels]
        categories = [str(c) for c in ctx.guild.categories]
        channels = [str(c) for c in ctx.guild.text_channels]
        vc = [str(c) for c in ctx.guild.voice_channels]
        emotes = [str(e) for e in ctx.guild.emojis]
        timezone_convert_creation = guild.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = guild.name, icon_url = guild.icon_url)
        embed.add_field(name = 'Owner:', value = f'{owner}', inline = True)
        embed.add_field(name = 'Server Created:', value = f'{creation}', inline = True)
        embed.add_field(name = '\u200b', value = '\u200b', inline = True)
        embed.add_field(name = 'Roles:', value = f'{len(roles)}\n(!roles to get list)', inline = True)
        embed.add_field(name = 'Emotes:', value = f'{len(emotes)}\n(!emotes to get list)', inline = True)
        embed.add_field(name = 'Members:', value = f'Total Members: {allmembers}\nMembers: {members}, Bots: {bots}', inline = True)
        embed.add_field(name = 'Channels:', value = f'Total Channels: {len(allchannels)}, Catergories: {len(categories)}, Text Channels: {len(channels)}, Voice Channels: {len(vc)}', inline = False)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #roleinfo
    @commands.command(aliases = ['role'])
    async def roleinfo(self, ctx, *, role: discord.Role):
        guild = self.client.get_guild(700559773028057098)
        date = datetime.datetime.now()
        if str(role.colour) == '#000000':
            color = 0xFCCB00
        else:
            color = role.colour
        memberlist = [str(m.mention) for m in role.members]
        timezone_convert_creation = role.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern'))
        creation = timezone_convert_creation.strftime('%B %d, %Y at %H:%M EST')
        id = role.id
        mentionable = role.mentionable
        embed = discord.Embed(color = color)
        embed.set_author(name = role.name, icon_url = guild.icon_url)
        embed.add_field(name = 'Role Created:', value = f'{creation}', inline = False)
        embed.add_field(name = 'ID', value = f'`{id}`', inline = True)
        embed.add_field(name = 'Mentionable?', value = f'{mentionable}', inline = True)
        embed.add_field(name = '# of Members:', value = f'{len(memberlist)}', inline = True)
        embed.set_footer(text = 'Use !rolelist to get a list of users with a role')
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @roleinfo.error
    async def roleinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            roleinfo_error = await ctx.send(f'Please state the role with the command')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await roleinfo_error.delete()

    #rolelist
    @commands.command()
    async def rolelist(self, ctx, *, role: discord.Role):
        guild = self.client.get_guild(700559773028057098)
        memberlist = [str(m.mention) for m in role.members]
        members = " ".join(memberlist)
        embed = discord.Embed(title = f'Members ({len(memberlist)}):', description = f'{members}', color = 0xFCCB00)
        embed.set_author(name = role.name, icon_url = guild.icon_url)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @rolelist.error
    async def rolelist_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            rolelist_error = await ctx.send(f'Please state the role with the command')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await rolelist_error.delete()

    #roles
    @commands.command()
    async def roles(self, ctx):
        guild = self.client.get_guild(700559773028057098)
        rolelist = [str(r.mention) for r in ctx.guild.roles if r != ctx.guild.default_role]
        role = " ".join(rolelist)
        embed = discord.Embed(title = 'Roles List:', description = f'{role}', color = 0xFCCB00)
        embed.set_footer(text = 'You might be looking for the !roleinfo command instead')
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #emotes
    @commands.command()
    async def emotes(self, ctx):
        guild = self.client.get_guild(700559773028057098)
        emotelist = [str(e) for e in ctx.guild.emojis]
        emotes = " ".join(emotelist)
        embed = discord.Embed(title = 'Emotes List:', description = f'{emotes}', color = 0xFCCB00)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #leafs last cup
    @commands.command()
    async def leafs(self, ctx):
        await ctx.message.delete()
        today = datetime.datetime.today()
        lastcup = datetime.datetime.strptime('05-02-1967', '%m-%d-%Y')
        threeone = datetime.datetime.strptime('05-31-2021', '%m-%d-%Y')
        serieswin = datetime.datetime.strptime('04-20-2004', '%m-%d-%Y')
        zamboni = datetime.datetime.strptime('02-22-2020', '%m-%d-%Y')
        cupdrought = datetime.datetime.strptime('07-04-2021', '%m-%d-%Y')
        lastcupdays = (today - lastcup).days
        threeonedays = (today - threeone).days
        serieswindays = (today - serieswin).days
        zambonidays = (today - zamboni).days
        cupdroughtdays = (cupdrought - today).days
        embed = discord.Embed(title = 'Leafs Stats!', description = "Welcome to the shitshow of the Toronto Maple Leafs! Here are some FUN STATS\nHere's some info to catch you up!\nhttps://www.youtube.com/watch?v=25j6s-ZY3mY", color = 0x00205B)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/818494514867077144/849804790511042560/pandaleafs.png')
        embed.add_field(name = f'{lastcupdays} days since winning a Cup', value = 'Last Cup Win: May 2nd, 1967', inline = False)
        embed.add_field(name = f'{threeonedays} days since blowing a 3-1 playoff lead to the Montreal Canadiens', value = 'Blew Series Lead On: May 31st, 2021', inline = False)
        embed.add_field(name = f'{serieswindays} days since winning a playoff series', value = 'Last Series Win: April 20, 2004', inline = False)
        embed.add_field(name = f'{zambonidays} days since losing to a 42 YEAR OLD ZAMBONI DRIVER THAT WORKS FOR YOUR MINOR LEAGUE AFFILIATE', value = 'Date Lost: April 22nd, 2020\nSteve Dangle: https://www.youtube.com/watch?v=QFnQ0dcaBUI', inline = False)
        if cupdroughtdays > 0:
            embed.add_field(name = f'{cupdroughtdays} days away from setting the record for the longest Stanley Cup drought in NHL History', value = 'Date to hit: July 4, 2021', inline = False)
        elif cupdroughtdays == 0:
            embed.add_field(name = 'THE LEAFS HAVE set the record for the longest Stanley Cup drought in NHL History', value = 'Date to hit: July 4, 2021', inline = False)
        elif cupdroughtdays < 0:
            embed.add_field(name = 'The Leafs now hold the record for the longest Stanley Cup Drought!')
        embed.set_footer(text = '#LeafsForever', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/849808217667665950/5a4fbbd0da2b4f099b95da1f.png')
        await ctx.send(embed = embed)

    #rules embed
    @commands.command()
    @commands.check(isitdev)
    async def rules(self, ctx):
        channel = self.client.get_channel(700571972362567763)
        title = discord.Embed(color = 0xFFCB00)
        title.set_image(url = 'https://cdn.discordapp.com/attachments/818494514867077144/843517482349363241/Rules_1.png')
        await channel.send(embed = title)
        embed = discord.Embed(color = 0xFFCB00)
        embed.add_field(name = '1️⃣: Be friendly and respectful to everyone.', value = '\u200b', inline = False)
        embed.add_field(name = '2️⃣: No racism, sexism, homophobia, and any other discriminatory or witch-hunting behavior, no attacks on politics or religion.', value = '\u200b', inline = False)
        embed.add_field(name = '3️⃣: No spam is tolerated.', value = '\u200b', inline = False)
        embed.add_field(name = '4️⃣: No NSFW content, including anything relating to inappropriate topics or playing them in a bot.', value = '\u200b', inline = False)
        embed.add_field(name = '5️⃣: Make sure all messages are on topic as per channel.', value = '\u200b', inline = False)
        embed.add_field(name = '6️⃣: Do not ever @ anyone without a good reason.', value = '\u200b', inline = False)
        embed.add_field(name = '7️⃣: Friendly banter and trolling is allowed, but straight-up bullying will NOT be tolerated.', value = '\u200b', inline = False)
        embed.add_field(name = "8️⃣: If you ever feel a moderation effort was given to you unfairly, or if you have a complaint, feel free to contact any moderator __through DMs.__", value = '\u200b', inline = False)
        embed.add_field(name = '9️⃣: Please try not to play any earrape or nsfw content in VCs, especially when someone else is present', value = '\u200b', inline = False)
        embed.add_field(name = '🔟: These rules are not perfect, do not try to use loopholes to your advantage. Just use common sense. Do not try the "Its not in the rules" excuse.', value = '\u200b', inline = False)
        embed.add_field(name = "*️⃣ Discord's ToS also applies to this server, refer to it here:", value = '👉 https://discord.com/new/terms \n\u200b', inline = False)
        embed.add_field(name = 'ABOUT', value = '*️⃣ This is the official Discord server for London Central Secondary School, and is meant for students attending LCSS . Although people from other schools are more than welcome, just note that most conversations and announcements in this server will pertain to LCSS.\n\u200b', inline = False)
        embed.add_field(name = 'INSTRUCTIONS FOR NEW MEMBERS', value = '*️⃣ Please select what grade and cohort you are in via <#700563120690561024>')
        await channel.send(embed = embed)
        await ctx.message.delete()

    #identification embed
    @commands.command()
    @commands.check(isitdev)
    async def idembed(self, ctx):
        channel = self.client.get_channel(700563120690561024)
        grade = discord.Embed(title = 'Identification Process', description = 'Please give yourself a grade and feel free to add a color as well!', color = 0xFFCB00)
        grade.add_field(name = '__Grade Selection:__', value = "🔵 - Grade 9\n🟢 - Grade 10\n🟣 - Grade 11\n🟡 - Grade 12\n\n🟠 - Alumni\n⚪ - Other School (Please only select this if you don't go to Central", inline = False)
        gradeembed = await channel.send(embed = grade)
        await gradeembed.add_reaction('🔵')
        await gradeembed.add_reaction('🟢')
        await gradeembed.add_reaction('🟣')
        await gradeembed.add_reaction('🟡')
        await gradeembed.add_reaction('🟠')
        await gradeembed.add_reaction('⚪')
        color = discord.Embed(color = 0xFFCB00)
        color.add_field(name = '__Color Selection:__', value = '<:pink:762810083791863820> - Pink\n🔴 - Red\n🟠 - Orange\n🟡 - Yellow\n🟢 - Green\n🔵 - Blue\n🟣 - Purple\n🟤 - Brown\n⚫ - Black\n⚪ - White', inline = False)
        colorembed = await channel.send(embed = color)
        await colorembed.add_reaction('<:pink:762810083791863820>')
        await colorembed.add_reaction('🔴')
        await colorembed.add_reaction('🟠')
        await colorembed.add_reaction('🟡')
        await colorembed.add_reaction('🟢')
        await colorembed.add_reaction('🔵')
        await colorembed.add_reaction('🟣')
        await colorembed.add_reaction('🟤')
        await colorembed.add_reaction('⚫')
        await colorembed.add_reaction('⚪')
        await ctx.message.delete()

    #cohortembed
    @commands.command()
    @commands.check(isitdev)
    async def cohortembed(self, ctx):
        channel = self.client.get_channel(700563120690561024)
        embed = discord.Embed(color = 0xFFCB00)
        embed.add_field(name = '__Cohort Selection:__', value = '\U0001F1E6 - Cohort A\n\U0001F1E7 - Cohort B\n\U0001F1E8 - Cohort C (Online)', inline = False)
        cohortembed = await channel.send(embed = embed)
        await cohortembed.add_reaction('\U0001F1E6')
        await cohortembed.add_reaction('\U0001F1E7')
        await cohortembed.add_reaction('\U0001F1E8')
        await ctx.message.delete()

def setup(client):
    client.add_cog(info(client))
