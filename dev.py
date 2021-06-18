import discord
import asyncio

from discord.ext import commands

class dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def logsEmbed(self, ctx, message, command):
        embed_logs = discord.Embed(title = command, color = 0xFFCB00)
        embed_logs.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed_logs.add_field(name = 'Message:', value = message, inline = False)
        return embed_logs

    async def userError(self, ctx, format):
        await ctx.message.delete()
        await ctx.send(f'Please use this format: {format}', delete_after = 5.0)

    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787

    def isitus(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 412316765918461955 or ctx.author.id == 226457061959925761 or ctx.author.id == 217099695472771083 or ctx.author.id == 433067676034793503 or ctx.author.id == 686970892902989841 or ctx.author.id == 325790134601646080 or ctx.author.id == 334081188228628492

#Interact with #general without pings
    @commands.command()
    @commands.check(isitus)
    async def interact(self, ctx, *, message: commands.clean_content):
        await ctx.message.delete()
        channel = self.client.get_channel(760284361814835200)
        logs = self.client.get_channel(818495619710320640)
        await channel.trigger_typing()
        await asyncio.sleep(3)
        await channel.send(message)
        await logs.send(embed = self.logsEmbed(ctx, message, '!interact'))
        await ctx.send('Message Sent!', delete_after = 5.0)

    @interact.error
    async def interact_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '!interact (Message)')

#Interact with #general with pings
    @commands.command()
    @commands.check(isitdev)
    async def ghost(self, ctx, *, message):
        await ctx.message.delete()
        channel = self.client.get_channel(760284361814835200)
        logs = self.client.get_channel(818495619710320640)
        await channel.trigger_typing()
        await asyncio.sleep(3)
        await channel.send(message)

        await logs.send(embed = self.logsEmbed(ctx, message, '!ghost'))
        await ctx.send('Message Sent!', delete_after = 5.0)

    @ghost.error
    async def ghost_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '!ghost (Message)')

#Selfpromote
    @commands.command()
    @commands.check(isitdev)
    async def selfpromote(self, ctx):
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name = 'botperms')
        await ctx.author.add_roles(role)
        await ctx.author.send('You have promoted yourself!')

    @selfpromote.error
    async def selfpromote_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()

#DM a user
    @commands.command()
    @commands.check(isitdev)
    async def dm(self, ctx, member: discord.Member, *, message):
        await ctx.message.delete()
        logs = self.client.get_channel(818495619710320640)
        await member.send(message)

        await logs.send(embed = self.logsEmbed(ctx, message, '!dm'))
        await ctx.send('Message Sent!', delete_after = 5.0)

    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '!dm (Member) (Message)')

#Ghost pinging
    @commands.command(aliases = ['gp'])
    @commands.check(isitdev)
    async def ghostping(self, ctx, *, member: discord.Member):
        await ctx.message.delete()
        logs = self.client.get_channel(818495619710320640)
        await ctx.send(member.mention, delete_after = 0.0)

        embed = discord.Embed(color = 0xFFCB00)
        embed.add_field(name = 'User that has been Ghost Pinged:', value = member.mention)
        await logs.send(embed = embed)

    @ghostping.error
    async def ghostping_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '!ghostping (Member)')

#Talk to any channel the bot has access to
    @commands.command()
    @commands.check(isitdev)
    async def talk(self, ctx, channelid, *, message):
        await ctx.message.delete()
        logs = self.client.get_channel(818495619710320640)
        channel = self.client.get_channel(int(channelid))
        await channel.trigger_typing()
        await asyncio.sleep(3)
        await channel.send(f'{message}')

        embed = self.logsEmbed(ctx, message, '!talk')
        embed.insert_field_at(index = 0, name = 'Channel:', value = channel.mention)
        await logs.send(embed = embed)
        await ctx.send('Message Sent!', delete_after = 5.0)

    @talk.error
    async def talk_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.userError(ctx, '!talk (Channel ID) (Message)')

def setup(client):
    client.add_cog(dev(client))