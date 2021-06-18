import discord
import asyncio
import datetime

from discord.ext import commands

class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787

    #Poll command
    @commands.command(aliases = ['vote'])
    @commands.has_role('Staff')
    async def poll(self, ctx, *, question):
        await ctx.message.delete()
        channel = self.client.get_channel(823041499259207690)
        date = datetime.datetime.now()
        embed = discord.Embed(title = '__Poll__', color = 0xFFCB00)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST')
        msg1 = await ctx.send(f'What is the first response option? You will have 2 response options at least and 5 at most.')
        try:
            a = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 30)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return
        await msg1.delete()
        await ctx.channel.purge(limit = 1)
        msg2 = await ctx.send(f'What is the second response option?')
        try:
            b = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 30)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return
        await msg2.delete()
        await ctx.channel.purge(limit = 1)
        msg3 = await ctx.send(f'What is the third response option? Type "Done" (It is case sensitive) if all response options are already given')
        try:
            c = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 30)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return
        await msg3.delete()
        await ctx.channel.purge(limit = 1)
        if c.content == 'Done':
            embed.add_field(name = f'Question: {question}', value = f'A: {a.content}\nB: {b.content}', inline = False)
            embed_b = await channel.send(embed = embed)
            await embed_b.add_reaction('\U0001F1E6')
            await embed_b.add_reaction('\U0001F1E7')
        else:
            msg4 = await ctx.send(f'What is the fourth response option? Type "Done" (It is case sensitive) if all response options are already given')
            try:
                d = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 30)
            except asyncio.TimeoutError:
                await ctx.send(f'Timed Out')
                return
            await msg4.delete()
            await ctx.channel.purge(limit = 1)
            if d.content == 'Done':
                embed.add_field(name = f'Question: {question}', value = f'A: {a.content}\nB: {b.content}\nC: {c.content}', inline = False)
                embed_c = await channel.send(embed = embed)
                await embed_c.add_reaction('\U0001F1E6')
                await embed_c.add_reaction('\U0001F1E7')
                await embed_c.add_reaction('\U0001F1E8')
            else:
                msg5 = await ctx.send(f'What is the final response option? Type "Done" (It is case sensitive) if all response options are already given')
                try:
                    e = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 30)
                except asyncio.TimeoutError:
                    await ctx.send(f'Timed Out')
                    return
                await msg5.delete()
                await ctx.channel.purge(limit = 1)
                if e.content == 'Done':
                    embed.add_field(name = f'Question: {question}', value = f'A: {a.content}\nB: {b.content}\nC: {c.content}\nD: {d.content}', inline = False)
                    embed_d = await channel.send(embed = embed)
                    await embed_d.add_reaction('\U0001F1E6')
                    await embed_d.add_reaction('\U0001F1E7')
                    await embed_d.add_reaction('\U0001F1E8')
                    await embed_d.add_reaction('\U0001F1E9')
                else:
                    embed.add_field(name = f'Question: {question}', value = f'A: {a.content}\nB: {b.content}\nC: {c.content}\nD: {d.content}\nE: {e.content}', inline = False)
                    embed_e = await channel.send(embed = embed)
                    await embed_e.add_reaction('\U0001F1E6')
                    await embed_e.add_reaction('\U0001F1E7')
                    await embed_e.add_reaction('\U0001F1E8')
                    await embed_e.add_reaction('\U0001F1E9')
                    await embed_e.add_reaction('\U0001F1EA')

    #countrefresh
    @commands.command(aliases = ['cr', 'crefresh'])
    @commands.has_role('Staff')
    async def countrefresh(self, ctx):
        guild = self.client.get_guild(700559773028057098)
        vc = self.client.get_channel(734139663903752292)
        members = len([m for m in ctx.guild.members if not m.bot])
        await vc.edit(reason = 'New User', name = '👻 Member Count: ' + str(members))
        await ctx.message.delete()

    #!ping command
    @commands.command(aliases = ['pong'])
    async def ping(self, ctx):
        ping = int(round(self.client.latency * 1000))
        msg = 'Pong! '+ str(ping)+ ' ms'
        embed = discord.Embed(title = 'Ping Latency', color = 0xFFCB00)
        embed.add_field(name = ':ping_pong:', value = (msg), inline = True)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #!gradeshuffle command
    @commands.command(aliases = ['gs'])
    @commands.check(isitdev)
    async def gradeshuffle(self, ctx):
        await ctx.send(f'Initiating Grade Shuffle.\nNote: Due to the massive amount of people in this server, it will take some time between each confirmation message.')
        guild = self.client.get_guild(700559773028057098)
        rolealumni = discord.utils.get(ctx.guild.roles, name = 'Alumni')
        role12 = discord.utils.get(ctx.guild.roles, name = 'Grade 12')
        role11 = discord.utils.get(ctx.guild.roles, name = 'Grade 11')
        role10 = discord.utils.get(ctx.guild.roles, name = 'Grade 10')
        role9 = discord.utils.get(ctx.guild.roles, name = 'Grade 9')
        for users in role12.members:
            await users.add_roles(rolealumni)
            await users.remove_roles(role12)
        await ctx.send(f'Grade 12s Done!')
        for users in role11.members:
            await users.add_roles(role12)
            await users.remove_roles(role11)
        await ctx.send(f'Grade 11s Done!')
        for users in role10.members:
            await users.add_roles(role11)
            await users.remove_roles(role10)
        await ctx.send(f'Grade 10s Done!')
        for users in role9.members:
            await users.add_roles(role10)
            await users.remove_roles(role9)
        await ctx.send(f'Grade 9s Done!')

    #!cohortpurge
    @commands.command(aliases = ['cp'])
    @commands.check(isitdev)
    async def cohortpurge(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'Purging all Cohort Roles in this server')
        A = discord.utils.get(ctx.guild.roles, name = 'Cohort A')
        B = discord.utils.get(ctx.guild.roles, name = 'Cohort B')
        C = discord.utils.get(ctx.guild.roles, name = 'Cohort C (Online)')
        for users in A.members:
            await users.remove_roles(A)
        await ctx.send(f'Cohort A purged')
        for users in B.members:
            await users.remove_roles(B)
        await ctx.send(f'Cohort B purged')
        for users in C.members:
            await users.remove_roles(C)
        await ctx.send(f'Cohort C purged')

    #roleping
    @commands.command()
    @commands.has_role('Staff')
    async def roleping(self, ctx, duration: int, *, role: discord.Role):
        await ctx.message.delete()
        privatechannels = ['700600677596004415', '847873556725628998', '745331414718742569', '701877914001735772']
        if ctx.message.channel.id in privatechannels:
            if duration <= 60 and duration > 0:
                role.edit(mentionable = True)
                await ctx.send(f'{role.name} will be pingable for the next {duration} seconds')
                asyncio.sleep(duration)
                role.edit(mentionable = False)
            else:
                await ctx.send(f'Error: Duration must be between 0-60 seconds')
        else:
            await ctx.send(f'You can not use this command here')

    #identification role removal
    @commands.command()
    @commands.has_role('Staff')
    async def idremove(self, ctx):
        await ctx.message.delete()
        guild = self.client.get_guild(700559773028057098)
        roleAlumni = discord.utils.get(guild.roles, name = 'Alumni')
        role12 = discord.utils.get(guild.roles, name = 'Grade 12')
        role11 = discord.utils.get(guild.roles, name = 'Grade 11')
        role10 = discord.utils.get(guild.roles, name = 'Grade 10')
        role9 = discord.utils.get(guild.roles, name = 'Grade 9')
        roleOtherSchools = discord.utils.get(guild.roles, name = 'Other Schools')
        roleIdentify = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')
        msg = await ctx.send('This may take a while')
        for member in guild.members:
            if roleIdentify in member.roles:
                if roleAlumni in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role12 in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role11 in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role10 in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role9 in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if roleOtherSchools in member.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')                                  
        await msg.edit(content = 'Identification Roles Removed!')

    #emergencystaffping
    def isitthem(ctx):
        return ctx.author.id == 772266273492041728 or ctx.author.id == 629807496210415655 or ctx.author.id == 498176822404579330 or ctx.author.id == 479411003881160707 or ctx.author.id == 524001661379936268 or ctx.author.id == 226457061959925761 or ctx.author.id == 325790134601646080

    @commands.command(aliases = ['sos'])
    @commands.check(isitthem)
    async def emergency(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send(f'Are you sure you want to ping Staff?')
        await msg.add_reaction('\U00002714')
        await msg.add_reaction('\U00002716')
        try:
            reaction, user = await ctx.bot.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) in ('\U00002714','\U00002716'), timeout = 30)
            if str(reaction.emoji) == '\U00002714':
                await ctx.send(f'<@&779814865371004948>')
            elif str(reaction.emoji) == '\U00002716':
                reply = await ctx.send(f"Ok, please don't try this again unless it's an emergency")
                await asyncio.sleep(5)
                await reply.delete()
            else:
                await ctx.send(f'DM <@524001661379936268> if you somehow got this error and tell him how')
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return

    #id
    @commands.command(aliases = ['identification'])
    async def id(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'Please go to <#700563120690561024> to identify yourself!')

    #pg
    @commands.command()
    async def pg(self, ctx):
        await ctx.send(f'**PLEASE KEEP IT HECCING PG**')
        await ctx.message.delete()

    #!st
    @commands.command(aliases = ['schooltalk'])
    async def st(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'Please go to <#771694740521091114> for school talk!')

    #!gen
    @commands.command(aliases = ['general'])
    async def gen(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'Please go to <#760284361814835200> for your conversation!')

    #bc
    @commands.command(aliases = ['botcommands'])
    async def bc(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'Please go to <#789619349903507456> for bot commands!')

    #meme
    @commands.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Please send these to <#760284416848298025> so you don't clog up this chat!")

def setup(client):
    client.add_cog(utilities(client))