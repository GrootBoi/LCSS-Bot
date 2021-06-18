import discord
import asyncio
import random
import json

from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #!hug
    @commands.command()
    async def hug(self, ctx, *, member: discord.Member):
        if member == ctx.author:
            await ctx.send(f'{ctx.author.mention} has hugged themselves!?')
            await ctx.message.delete()
        elif member.id == 773215529082159135:
            await ctx.message.delete()
            await ctx.send(f'Thank You for the hug! :heart: <:pandahug:776186238213554187>')
            await asyncio.sleep(5)
            await ctx.send(f'Lemme give you a hug back {ctx.author.mention} :heart: <:pandahug:776186238213554187>')
        else:
            await ctx.send(f'{ctx.author.mention} has given {member.mention} a hug! :heart: <:pandahug:776186238213554187>')
            await ctx.message.delete()

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            hug_user_error = await ctx.send(f'{ctx.author.mention} has given... wait a minute, who are you hugging? Please specify a user!')
            await ctx.message.delete()

    #!boyuan
    @commands.command()
    async def boyuan(self, ctx):
        msg = await ctx.send(f'Go Fuck Yourself <@412316765918461955>')
        await ctx.message.delete()
        await msg.edit(content = f'Go Fuck Yourself Botanist')
        await msg.edit(content = f'Go Fuck Yourself Cumstain')
        await msg.edit(content = f'Go Fuck Yourself Boyuan')
        await msg.edit(content = f'Go Fuck Yourself Boycash')
        await msg.edit(content = f'Go Fuck Yourself Buoyancy')
        await msg.edit(content = f'Go Fuck Yourself Boyuan')

    #!bam
    @commands.command(aliases = ['bang'])
    async def bam(self, ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send(f'BANG!?! {ctx.author.mention} has thrown a ~~axe~~ boommerang at their head')
            await ctx.message.delete()
        elif member.id == 773215529082159135:
            await ctx.send(f'BANGG!!! {ctx.author.mention} has thrown an axe at... wait where is it?')
            await ctx.message.delete()
        else:
            await ctx.send(f'BANGG!!! {ctx.author.mention} has thrown an axe at {member.mention}')
            await ctx.message.delete()
            value = random.randint(1, 10)
            if value > 8:
                question = await ctx.send(f'AND IT HAS HIT THEM! They are down and critically injured\nWould you like to finish them? React quickly!')
                await question.add_reaction('\U00002714')
                await question.add_reaction('\U00002716')
                try:
                    reaction, user = await ctx.bot.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) in ('\U00002714','\U00002716'), timeout = 5)
                    if str(reaction.emoji) == '\U00002714':
                        await question.delete()
                        await ctx.send(f"You pull out another axe and uh yeah, let's just say their head isn't attached anymore")
                    elif str(reaction.emoji) == '\U00002716':
                        await ctx.send(f"Ok nice guy, why'd you throw the axe at them in the first place? Now drag them to the hospital")
                except asyncio.TimeoutError:
                    await ctx.send(f"You're too slow! {member.mention} has pulled out their revolver and headshotted you!")
            else:
                await ctx.send(f"HAHA You suck, you missed and you can't aim. {member.mention} it's your turn to take a shot now. Use command `!bam @User`")

    @bam.error
    async def bam_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            bam_user_error = await ctx.send(f'BANG???{ctx.author.mention} has thrown a hammer at something or someone but clearly did not know how to aim. Please specify the user to hit')
            await ctx.message.delete()

    #!kill
    @commands.command()
    async def kill(self, ctx, *, member: discord.Member):
        if member == ctx.author:
            await ctx.send(f'{member.mention} has been killed, after further investigation this has been listed as a suicide.')
            await ctx.message.delete()
        elif member.id == 773215529082159135:
            await ctx.send(f'{ctx.author.mention} has been killed, it seems as though they were killed by a turn table...')
            await ctx.message.delete()
        else:
            await ctx.send(f'DEAD BODY!!!! {member.mention} has been killed, the suspect is still on the loose!')
            await ctx.message.delete()

    @kill.error
    async def kill_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            kill_user_error = await ctx.send(f'{ctx.author.mention} has been arrested for attempted murder. They were walking around stabbing the air with a knife. Probably on drugs.')
            await ctx.message.delete()

    #!revive
    @commands.command()
    async def revive(self, ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send(f'{member.mention} has attempted to revive themself, they have clearly failed and is more dead than ever.')
            await ctx.message.delete()
        else:
            await ctx.send(f'{member.mention} has been revived by {ctx.author.mention}!')
            await ctx.message.delete()

    @revive.error
    async def revive_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            revive_user_error = await ctx.send(f'What are you trying revive? The air?')
            await ctx.message.delete()

    #fys
    @commands.command(aliases = ['fuckoff'])
    async def fys(self, ctx, *, member: discord.Member):
        if member.id == 773215529082159135:
            await ctx.message.delete()
            await ctx.send(f'No you go fuck yourself {ctx.author.mention}')
        elif member.id == 524001661379936268:
            await ctx.message.delete()
            await ctx.send(f'No you go fuck yourself {ctx.author.mention}')
        else:
            await ctx.message.delete()
            await ctx.send(f'{ctx.author.mention} has told {member.mention} to fuck themselves')

    @fys.error
    async def fys_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            fys_user_error = await ctx.send(f'{ctx.author.mention} Please state who you want to fuck.')
            await ctx.message.delete()

    #!bann
    @commands.command()
    async def bann(self, ctx, member: discord.Member, *, reason = None):
        embed = discord.Embed(color = 0xFFCB00)
        embed.add_field(name = f'{member.name} has been bannned by {ctx.author.name}', value = f' For reason:\n\n{reason}')
        await ctx.send(embed = embed)
        await ctx.message.delete()

    #rock paper scissors
    @commands.command(aliases = ['rps'])
    async def rockpaperscissors(self, ctx):
        result = 'An unknown error has occurred'
        await ctx.message.delete()
        with open('rps.json', 'r') as f:
            data = json.load(f)
            if str(ctx.author.id) not in data:
                data[str(ctx.author.id)] = []
                data[str(ctx.author.id)].append({
                    'wins': 0,
                    'ties': 0,
                    'loses': 0
                })
                with open('rps.json', 'w') as f:
                    json.dump(data, f, indent = 4)
            for num in data[str(ctx.author.id)]:
                wins = int(num['wins'])
                ties = int(num['ties'])
                loses = int(num['loses'])
        userresponses = ['rock', 'paper', 'scissors', 'r', 'p', 's']
        botresponses = ['rock', 'paper', 'scissors']
        title = 'Rock Paper Scissors'
        start = discord.Embed(title = title, description = 'Type in your repsonse when I say shoot. (R, P, S)', color = 0xFFCB00)
        rock = discord.Embed(title = title, description = 'Rock', color = 0xFFCB00)
        paper = discord.Embed(title = title, description = 'Paper', color = 0xFFCB00)
        scissors = discord.Embed(title = title, description = 'Scissors', color = 0xFFCB00)
        shoot = discord.Embed(title = title, description = 'SHOOT!', color = 0xFFCB00)
        msg = await ctx.send(embed = start)
        await asyncio.sleep(3)
        await msg.edit(embed = rock)
        await asyncio.sleep(1)
        await msg.edit(embed = paper)
        await asyncio.sleep(1)
        await msg.edit(embed = scissors)
        await asyncio.sleep(1)
        await msg.edit(embed = shoot)
        try:
            user = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 15)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return
        if user.content.lower() in userresponses:
            bot = random.choice(botresponses)
            if str(bot) == 'rock':
                await ctx.send('Rock')
                if user.content.lower() == 'paper' or user.content.lower() == 'p':
                    result = 'You won!'
                    wins = (wins + 1)
                elif user.content.lower() == 'rock' or user.content.lower() == 'r':
                    result = "It's a draw"
                    ties = (ties + 1)
                elif user.content.lower() == 'scissors' or user.content.lower() == 's':
                    result = 'You lost.'
                    loses = (loses + 1)
            elif str(bot) == 'scissors':
                await ctx.send('Scissors')
                if user.content.lower() == 'rock' or user.content.lower() == 'r':
                    result = 'You won!'
                    wins = (wins + 1)
                elif user.content.lower() == 'scissors' or user.content.lower() == 's':
                    result = "It's a draw"
                    ties = (ties + 1)
                elif user.content.lower() == 'paper' or user.content.lower() == 'p':
                    result = 'You lost.'
                    loses = (loses + 1)
            elif str(bot) == 'paper':
                await ctx.send('Paper')
                if user.content.lower() == 'scissors' or user.content.lower() == 's':
                    result = 'You won!'
                    wins = (wins + 1)
                elif user.content.lower() == 'paper' or user.content.lower() == 'p':
                    result = "It's a draw"
                    ties = (ties + 1)
                elif user.content.lower() == 'rock' or user.content.lower() == 'r':
                    result = 'You lost.'
                    loses = (loses + 1)
            else:
                result = 'Error: Bot Response Chosen'
        else:
            await ctx.send(f'You have typed an invalid option! You lost.')
            result = 'You lost.'
            loses = (loses + 1)
        description = f'Your record in RPS is {wins} - {ties} - {loses}'
        record = discord.Embed(title = result, description = description, color = 0xFFCB00)
        await ctx.send(embed = record)
        with open('rps.json', 'r') as f:
            data = json.load(f)
            data[str(ctx.author.id)] = []
            data[str(ctx.author.id)].append({
                'wins': wins,
                'ties': ties,
                'loses': loses
            })
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent = 4)

    #rock paper scissors lizard spock
    @commands.command()
    async def rpsls(self, ctx):
        result = 'An unknown error has occurred'
        await ctx.message.delete()
        with open('rpsls.json', 'r') as f:
            data = json.load(f)
            if str(ctx.author.id) not in data:
                data[str(ctx.author.id)] = []
                data[str(ctx.author.id)].append({
                    'wins': 0,
                    'ties': 0,
                    'loses': 0
                })
                with open('rpsls.json', 'w') as f:
                    json.dump(data, f, indent = 4)
            for num in data[str(ctx.author.id)]:
                wins = int(num['wins'])
                ties = int(num['ties'])
                loses = int(num['loses'])

        userresponses = ['rock', 'paper', 'scissors', 'lizard', 'spock', 'r', 'p', 'sc', 'l', 'sp']
        botresponses = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        r = ['rock', 'r']
        p = ['paper', 'p']
        sc = ['scissors', 'sc']
        l = ['lizard', 'l']
        sp = ['spock', 'sp']

        def win(self, wins):
            result = 'You won!'
            wins += 1
            return result, wins

        def tie(self, ties):
            result = "It's a draw"
            ties += 1
            return result, ties

        def lose(self, loses):
            result = 'You lost.'
            loses += 1
            return result, loses
        
        title = 'Rock Paper Scissors Lizard Spock'
        start = discord.Embed(title = title, description = 'Type in your repsonse when I say shoot. (R, P, Sc, L, Sp)', color = 0xFFCB00)
        start.set_footer(text = 'If you have no idea what this is, use command !rpslsinfo')
        rock = discord.Embed(title = title, description = 'Rock', color = 0xFFCB00)
        paper = discord.Embed(title = title, description = 'Paper', color = 0xFFCB00)
        scissors = discord.Embed(title = title, description = 'Scissors', color = 0xFFCB00)
        lizard = discord.Embed(title = title, description = 'Lizard', color = 0xFFCB00)
        spock = discord.Embed(title = title, description = 'Spock', color = 0xFFCB00)
        shoot = discord.Embed(title = title, description = '**SHOOT!**', color = 0xFFCB00)
        msg = await ctx.send(embed = start)
        await asyncio.sleep(4)
        await msg.edit(embed = rock)
        await asyncio.sleep(0.75)
        await msg.edit(embed = paper)
        await asyncio.sleep(0.75)
        await msg.edit(embed = scissors)
        await asyncio.sleep(0.75)
        await msg.edit(embed = lizard)
        await asyncio.sleep(0.75)
        await msg.edit(embed = spock)
        await asyncio.sleep(0.75)
        await msg.edit(embed = shoot)
        try:
            user = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 15)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return

        if user.content.lower() in userresponses:
            bot = random.choice(botresponses)
            if str(bot) == 'rock':
                await ctx.send('Rock')
                if user.content.lower() in p or user.content.lower() in sp:
                    result, wins = win(self, wins)
                elif user.content.lower() in r:
                    result, ties = tie(self, ties)
                elif user.content.lower() in sc or user.content.lower() in l:
                    result, loses = lose(self, loses)
            elif str(bot) == 'scissors':
                await ctx.send('Scissors')
                if user.content.lower() in r or user.content.lower() in sp:
                    result, wins = win(self, wins)
                elif user.content.lower() in sc:
                    result, ties = tie(self, ties)
                elif user.content.lower() in p or user.content.lower() in l:
                    result, loses = lose(self, loses)
            elif str(bot) == 'paper':
                await ctx.send('Paper')
                if user.content.lower() in l or user.content.lower() in sc:
                    result, wins = win(self, wins)
                elif user.content.lower() in p:
                    result, ties = tie(self, ties)
                elif user.content.lower() in r or user.content.lower() in sp:
                    result, loses = lose(self, loses)
            elif str(bot) == 'lizard':
                await ctx.send('Lizard')
                if user.content.lower() in sc or user.content.lower() in r:
                    result, wins = win(self, wins)
                elif user.content.lower() in l:
                    result, ties = tie(self, ties)
                elif user.content.lower() in p or user.content.lower() in sp:
                    result, loses = lose(self, loses)
            elif str(bot) == 'spock':
                await ctx.send('Spock')
                if user.content.lower() in l or user.content.lower() in p:
                    result, wins = win(self, wins)
                elif user.content.lower() in sp:
                    result, ties = tie(self, ties)
                elif user.content.lower() in sc or user.content.lower() in r:
                    result, loses = lose(self, loses)
            else:
                result = 'Error: Bot Response Chosen'

        else:
            await ctx.send(f'You have typed an invalid option! You lost.')
            lose(loses)
        description = f'Your record in RPSLS is {wins} - {ties} - {loses}'
        record = discord.Embed(title = result, description = description, color = 0xFFCB00)
        await ctx.send(embed = record)
        with open('rpsls.json', 'r') as f:
            data = json.load(f)
            data[str(ctx.author.id)] = []
            data[str(ctx.author.id)].append({
                'wins': wins,
                'ties': ties,
                'loses': loses
            })
            with open('rpsls.json', 'w') as f:
                json.dump(data, f, indent = 4)

    #rpslsinfo
    @commands.command()
    async def rpslsinfo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Info about RPSLS', color = 0xFFCB00)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/818494514867077144/853816412714958858/image0.png')
        await ctx.send(embed = embed)

    #rpsstats
    @commands.command(aliases = ['rpsstats'])
    async def rockpaperscissorsstats(self, ctx, *, member: discord.Member = None):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        with open('rps.json', 'r') as f:
            rps = json.load(f)
            if str(member.id) not in rps:
                wins1, ties1, loses1 = [0, 0, 0]
                value1 = 'No Stats'
                winrate1 = '-'
            else:
                for num in rps[str(member.id)]:
                    wins1 = int(num['wins'])
                    ties1 = int(num['ties'])
                    loses1 = int(num['loses'])
                    winrate1 = round(wins1/(wins1+ties1+loses1)*100)
                    value1 = f'{wins1} wins, {ties1} ties, {loses1} loses'
        with open('rpsls.json', 'r') as g:
            rpsls = json.load(g)
            if str(member.id) not in rpsls:
                wins2, ties2, loses2 = [0, 0, 0]
                value2 = 'No Stats'
                winrate2 = '-'
            else:
                for num in rpsls[str(member.id)]:
                    wins2 = int(num['wins'])
                    ties2 = int(num['ties'])
                    loses2 = int(num['loses'])
                    winrate2 = round(wins2/(wins2+ties2+loses2)*100)
                    value2 = f'{wins2} wins, {ties2} ties, {loses2} loses'

        if (wins1 + wins2 + ties1 + ties2 + loses1 + loses2) == 0:
            totalwinrate = '0%'
        else:
            totalwinrate = f'{round((wins1 + wins2)/(wins1 + wins2 + ties1 + ties2 + loses1 + loses2)*100)}%'

        embed = discord.Embed(title = 'All RPS Stats', color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator, icon_url = member.avatar_url)
        embed.add_field(name = '__Total Stats:__', value = f'{wins1 + wins2} wins, {ties1 + ties2} ties, {loses1 + loses2} loses')
        embed.add_field(name = '__Total Winrate:__', value = totalwinrate)
        embed.add_field(name = '\u200b', value = '\u200b')
        embed.add_field(name = 'RPS Stats:', value = value1)
        embed.add_field(name = 'RPS Winrate:', value = f'{winrate1}%')
        embed.add_field(name = '\u200b', value = '\u200b')
        embed.add_field(name = 'RPSLS Stats:', value = value2)
        embed.add_field(name = 'RPS Winrate:', value = f'{winrate2}%')
        embed.add_field(name = '\u200b', value = '\u200b')
        await ctx.send(embed = embed)

    #8ball
    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *, question):
        await ctx.message.delete()
        responses = ['It is Certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
        'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(title = '🎱 8 Ball!', description = f'Question: **__{question}__**\nBy: {ctx.author.mention}' , color = 0xFFCB00)
        embed.add_field(name = 'Response:', value = random.choice(responses))
        await ctx.send(embed = embed)
        
def setup(client):
    client.add_cog(fun(client))
