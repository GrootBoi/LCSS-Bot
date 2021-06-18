import discord
import asyncio
import datetime
import json
from discord import member
from discord.ext import commands, tasks

class test(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787

    #SHUT UP BOYUAN
    @commands.Cog.listener()
    async def on_typing(self, channel: discord.TextChannel, member: discord.Member, when):
        if channel.guild.id == 700559773028057098:
            if member.id == 412316765918461955:
                msg = await channel.send(f'SHUT THE UP BOYUAN, DONT EVEN FINISH TYPING')
                await asyncio.sleep(8)
                await msg.delete()

    #!test
    @commands.command()
    @commands.check(isitdev)
    async def test(self, ctx, *, emote: discord.Emoji):
        msg = ctx.send(f'{emote.emoji}')
        await msg.add_reaction(f'<:{emote.name}:{emote.id}>')

    @commands.command()
    @commands.check(isitdev)
    async def react(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Hi')
        test = await ctx.send(embed = embed)
        await test.add_reaction('◀️')
        await test.add_reaction('❌')
        if await self.client.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) not in ('❌')):
            await test.delete()
    
    @commands.command()
    @commands.check(isitdev)
    async def embedtesting(self, ctx, member: discord.Member):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Welcome fellow Golden Ghost!', description = 'Please read <#700571972362567763> and enjoy your stay!', color = 0xFFCB00)
        embed.set_author(name = f'{member.name}#{member.discriminator}', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
            
def setup(client):
    client.add_cog(test(client))

