import discord
import asyncio
import random
import datetime

from discord.ext import commands
from jasper import db

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    rps = db["RPS"]
    rpsls = db["RPSLS"]
    stat = db["Stats"]
    
#Hug
    @commands.command()
    async def hug(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        if member == ctx.author:
            await ctx.send(f'{ctx.author.mention} has hugged themselves!?')
        elif member.id == 773215529082159135:
            await ctx.send(f'Thank You for the hug! :heart: <:pandahug:776186238213554187>')
            await asyncio.sleep(5)
            await ctx.send(f'Lemme give you a hug back {ctx.author.mention} :heart: <:pandahug:776186238213554187>')
        else:
            await ctx.send(f'{ctx.author.mention} has given {member.mention} a hug! :heart: <:pandahug:776186238213554187>')

    @hug.error
    async def hug_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} has given... wait a minute, who are you hugging? Please specify a user!')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f'{ctx.author.mention} has given a hug to the air! Now, I assume you want to specify a real user?')

#Boyuan
    @commands.command()
    async def boyuan(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send('Go Fuck Yourself <@412316765918461955>')
        await msg.edit(content = 'Go Fuck Yourself Botanist')
        await msg.edit(content = 'Go Fuck Yourself Cumstain')
        await msg.edit(content = 'Go Fuck Yourself Boycash')
        await msg.edit(content = 'Go Fuck Yourself Boyuan')
        await msg.edit(content = 'Go Fuck Yourself Boylan')
        await msg.edit(content = 'Go Fuck Yourself Buoyancy')
        await msg.edit(content = 'Go Fuck Yourself Boyuan')

#Bam
    @commands.command(aliases = ['bang'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def bam(self, ctx, member: commands.MemberConverter):
        await ctx.message.delete()
        if member == ctx.author:
            await ctx.send(f'BANG!?! {ctx.author.mention} has thrown a ~~axe~~ boommerang at their head')
        elif member.id == 773215529082159135:
            await ctx.send(f'BANGG!!! {ctx.author.mention} has thrown an axe at... wait where is it?')
        else:
            await ctx.send(f'BANGG!!! {ctx.author.mention} has thrown an axe at {member.mention}')
            value = random.randint(1, 10)
            if value > 8:
                question = await ctx.send(f'AND IT HAS HIT THEM! They are down and critically injured\nWould you like to finish them? React quickly!')
                await question.add_reaction('\U00002714')
                await question.add_reaction('\U00002716')
                try:
                    reaction, user = await ctx.bot.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) in ('\U00002714','\U00002716'), timeout = 3)
                    if str(reaction.emoji) == '\U00002714':
                        await question.delete()
                        await ctx.send(f"You pull out another axe and uh yeah, let's just say their head isn't attached anymore")

                        usera = {"_id": ctx.author.id}
                        if (self.stat.count_documents(usera) == 0):
                            kills = 1
                            deaths = 0
                            revives = 0
                            statctx = {"_id": ctx.author.id, "kills": kills, "deaths": deaths, "revives": revives}
                            self.stat.insert_one(statctx)
                        else:
                            for result in self.stat.find(usera):
                                kills = int(result["kills"])
                            kills += 1
                            self.stat.update_one({"_id": ctx.author.id}, {"$set":{"kills": kills}})

                        userb = {"_id": member.id}
                        if (self.stat.count_documents(userb) == 0):
                            kills = 0
                            deaths = 1
                            revives = 0
                            statctx = {"_id": member.id, "kills": kills, "deaths": deaths, "revives": revives}
                            self.stat.insert_one(statctx)
                        else:
                            for result in self.stat.find(userb):
                                deaths = int(result["deaths"])
                            deaths += 1
                            self.stat.update_one({"_id": member.id}, {"$set":{"deaths": deaths}})

                    elif str(reaction.emoji) == '\U00002716':
                        await ctx.send(f"Ok nice guy, why'd you throw the axe at them in the first place? Now drag them to the hospital")

                except asyncio.TimeoutError:
                    await ctx.send(f"You're too slow! {member.mention} has pulled out their revolver and headshotted you!")
            else:
                await ctx.send(f"HAHA You suck, you missed and you can't aim. {member.mention} it's your turn to take a shot now. Use command `!bam @User`")

    @bam.error
    async def bam_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'BANG???{ctx.author.mention} has thrown a hammer at something or someone but clearly did not know how to aim. Please specify the user to hit')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f'BANGG!!! {ctx.author.mention} has thrown an axe at a ghost. OW! Oh that went through me.\nCAN YOU PLEASE THROW IT AT A REAL USER PLEASE?')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'You are on cooldown! Try again in {error.retry_after:.2f}s', delete_after = 5.0)

#Kill
    @commands.command()
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def kill(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        if member == ctx.author:
            await ctx.send(f'{member.mention} has been killed, after further investigation this has been listed as a suicide.')

            user = {"_id": ctx.author.id}
            if (self.stat.count_documents(user) == 0):
                kills = 1
                deaths = 1
                revives = 0
                statctx = {"_id": ctx.author.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(user):
                    kills = int(result["kills"])
                    deaths = int(result["deaths"])
                kills += 1
                deaths += 1
                self.stat.update_one({"_id": ctx.author.id}, {"$set":{"kills": kills}})
                self.stat.update_one({"_id": ctx.author.id}, {"$set":{"deaths": deaths}})

        elif member.id == 773215529082159135:
            await ctx.send(f'{ctx.author.mention} has been killed, it seems as though they were killed by a turn table...')

            usera = {"_id": 773215529082159135}
            if (self.stat.count_documents(usera) == 0):
                kills = 1
                deaths = 0
                revives = 0
                statctx = {"_id": 773215529082159135, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(usera):
                    kills = int(result["kills"])
                kills += 1
                self.stat.update_one({"_id": 773215529082159135}, {"$set":{"kills": kills}})

            userb = {"_id": ctx.author.id}
            if (self.stat.count_documents(userb) == 0):
                kills = 0
                deaths = 1
                revives = 0
                statctx = {"_id": ctx.author.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(userb):
                    deaths = int(result["deaths"])
                deaths += 1
                self.stat.update_one({"_id": ctx.author.id}, {"$set":{"deaths": deaths}})

        else:
            await ctx.send(f'DEAD BODY!!!! {member.mention} has been killed, the suspect is still on the loose!')

            usera = {"_id": ctx.author.id}
            if (self.stat.count_documents(usera) == 0):
                kills = 1
                deaths = 0
                revives = 0
                statctx = {"_id": ctx.author.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(usera):
                    kills = int(result["kills"])
                kills += 1
                self.stat.update_one({"_id": ctx.author.id}, {"$set":{"kills": kills}})

            userb = {"_id": member.id}
            if (self.stat.count_documents(userb) == 0):
                kills = 0
                deaths = 1
                revives = 0
                statctx = {"_id": member.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(userb):
                    deaths = int(result["deaths"])
                deaths += 1
                self.stat.update_one({"_id": member.id}, {"$set":{"deaths": deaths}})

    @kill.error
    async def kill_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} has been arrested for attempted murder. They were walking around stabbing the air with a knife. Probably on drugs.')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f'{ctx.author.mention} has been arrested for being under illegal substances. They claimed that they were killing someone but they were just stabbing a tree.')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'You are on cooldown! Try again in {error.retry_after:.2f}s', delete_after = 5.0)

#Revive
    @commands.command()
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def revive(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        if member == ctx.author:
            await ctx.send(f'{member.mention} has attempted to revive themself, they have clearly failed and is more dead than ever.')

            user = {"_id": ctx.author.id}
            if (self.stat.count_documents(user) == 0):
                kills = 0
                deaths = 1
                revives = 0
                statctx = {"_id": ctx.author.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(user):
                    deaths = int(result["deaths"])
                deaths += 1
                self.stat.update_one({"_id": ctx.author.id}, {"$set":{"deaths": deaths}})

        else:
            await ctx.send(f'{member.mention} has been revived by {ctx.author.mention}!')

            user = {"_id": member.id}
            if (self.stat.count_documents(user) == 0):
                kills = 0
                deaths = 0
                revives = 1
                statctx = {"_id": member.id, "kills": kills, "deaths": deaths, "revives": revives}
                self.stat.insert_one(statctx)
            else:
                for result in self.stat.find(user):
                    revives = int(result["revives"])
                revives += 1
                self.stat.update_one({"_id": member.id}, {"$set":{"revives": revives}})

    @revive.error
    async def revive_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('What are you trying revive? The air?')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("I'm fairly sure you just summoned some random dead guy. Call Constantine for help")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'You are on cooldown! Try again in {error.retry_after:.2f}s', delete_after = 5.0)

#Life Stats
    @commands.command()
    async def stats(self, ctx, *, member: commands.MemberConverter = None):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        
        user = {"_id": member.id}
        if (self.stat.count_documents(user) == 0):
            kills = 0
            deaths = 0
            revives = 0
        else:
            for result in self.stat.find(user):
                kills = int(result["kills"])
                deaths = int(result["deaths"])
                revives = int(result["revives"])
            self.stat.update_one({"_id": member.id}, {"$set":{"kills": kills}})
            self.stat.update_one({"_id": member.id}, {"$set":{"deaths": deaths}})
            self.stat.update_one({"_id": member.id}, {"$set":{"revives": revives}})

        embed = discord.Embed(title = 'Life Stats', color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator, icon_url = member.avatar_url)
        embed.add_field(name = 'Kills:', value = kills)
        embed.add_field(name = 'Deaths:', value = deaths)
        embed.add_field(name = 'Revives:', value = revives)
        if deaths == 0:
            embed.add_field(name = 'Kills per Death (K/D):', value = '∞')
        else:
            embed.add_field(name = 'Kills per Death (K/D):', value = round(kills/deaths, 2))
        if revives - deaths > 0:
            embed.add_field(name = 'Alive?', value = 'Yes')
        elif revives - deaths < 0:
            embed.add_field(name = 'Alive?', value = 'No')
        elif revives - deaths == 0:
            embed.add_field(name = 'Alive?', value = 'Just Barely')
        await ctx.send(embed = embed)        

#Fuck yourself
    @commands.command(aliases = ['fuckoff', 'gfys'])
    async def fys(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        if member.id == 773215529082159135 or member.id == 524001661379936268:
            await ctx.send(f'No you go fuck yourself {ctx.author.mention}')
        else:
            await ctx.send(f'{ctx.author.mention} has told {member.mention} to fuck themselves')

    @fys.error
    async def fys_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} Please state who you want to fuck.')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f'{ctx.author.mention} Look, they DONT EVEN EXIST. Mention a real user **please**')

#Fake Ban
    @commands.command()
    async def bann(self, ctx, member: commands.MemberConverter, *, reason = None):
        await ctx.message.delete()
        date = datetime.datetime.now()
        embed = discord.Embed(color = 0xFFCB00)
        embed.set_author(name = member.name + '#' + member.discriminator + ' has been bannned', icon_url = member.avatar_url)
        embed.add_field(name = 'For reason:', value = reason, inline = True)
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        await ctx.send(embed = embed)

    @bann.error
    async def bann_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('I SHALL BAN- uh, who? Please state the user to be bannned')
        elif isinstance(error, commands.MemberNotFound):
            date = datetime.datetime.now()
            embed = discord.Embed(color = 0xFFCB00)
            embed.set_author(name = 'A ghost user has been bannned', icon_url = 'https://media.discordapp.net/attachments/818494514867077144/844997139280822332/image0.jpg')
            embed.add_field(name = 'For reason:', value = f"{ctx.author.mention} has no idea what they're doing", inline = True)
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await ctx.send(embed = embed)

#Rock Paper Scissors
    @commands.command(aliases = ['rps'])
    async def rockpaperscissors(self, ctx):
        await ctx.message.delete()
        result = 'An unknown error has occurred'
        userresponses = ['rock', 'paper', 'scissors', 'r', 'p', 's']
        botresponses = ['Rock', 'Paper', 'Scissors']
        r = ['rock', 'r']
        p = ['paper', 'p']
        s = ['scissors', 's']
        start = discord.Embed(title = 'Rock Paper Scissors', description = 'Type in your repsonse when I say shoot. (R, P, S)', color = 0xFFCB00)
        rock = discord.Embed(title = 'Rock Paper Scissors', description = 'Rock', color = 0xFFCB00)
        paper = discord.Embed(title = 'Rock Paper Scissors', description = 'Paper', color = 0xFFCB00)
        scissors = discord.Embed(title = 'Rock Paper Scissors', description = 'Scissors', color = 0xFFCB00)
        shoot = discord.Embed(title = 'Rock Paper Scissors', description = '**SHOOT!**', color = 0xFFCB00)
        sending = [rock, paper, scissors, shoot]

        user = {"_id": ctx.author.id}
        if (self.rps.count_documents(user) == 0):
            wins = 0
            ties = 0
            loses = 0
            rpsctx = {"_id": ctx.author.id, "wins": wins, "ties": ties, "loses": loses}
            self.rps.insert_one(rpsctx)
        else:
            for result in self.rps.find(user):
                wins = result["wins"]
                ties = result["ties"]
                loses = result["loses"]
        
        msg = await ctx.send(embed = start)
        await asyncio.sleep(3)
        for x in sending:
            await msg.edit(embed = x)
            await asyncio.sleep(1)
        try:
            user = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 15)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return

        if user.content.lower() in userresponses:
            bot = random.choice(botresponses)
            await ctx.send(bot)
            if bot == 'Rock' and user.content.lower() in p or bot == 'Scissors' and user.content.lower() in r or bot == 'Paper' and user.content.lower() in s:
                result = 'You won!'
                wins += 1
                self.rps.update_one({"_id": ctx.author.id}, {"$set":{"wins":wins}})
            elif bot == 'Rock' and user.content.lower() in r or bot == 'Scissors' and user.content.lower() in s or bot == 'Paper' and user.content.lower() in p:
                result = "It's a draw"
                ties += 1
                self.rps.update_one({"_id": ctx.author.id}, {"$set":{"ties":ties}})
            elif bot == 'Rock' and user.content.lower() in s or bot == 'Scissors' and user.content.lower() in p or bot == 'Paper' and user.content.lower() in r:
                result = 'You lost.'
                loses += 1
                self.rps.update_one({"_id": ctx.author.id}, {"$set":{"loses":loses}})
        else:
            await ctx.send('You have typed an invalid option! You lost.')
            result = 'You lost.'
            loses += 1
            self.rps.update_one({"_id": ctx.author.id}, {"$set":{"loses":loses}})

        record = discord.Embed(title = result, description = f'Your record in RPS is {wins} - {ties} - {loses}', color = 0xFFCB00)
        await ctx.send(embed = record)

#Rock Paper Scissors Lizard Spock
    @commands.command(aliases = ['rpsls'])
    async def rps5(self, ctx):
        await ctx.message.delete()
        result = 'An unknown error has occurred'
        userresponses = ['rock', 'paper', 'scissors', 'lizard', 'spock', 'r', 'p', 'sc', 'l', 'sp']
        botresponses = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        r = ['rock', 'r']
        p = ['paper', 'p']
        sc = ['scissors', 'sc']
        l = ['lizard', 'l']
        sp = ['spock', 'sp']
        start = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Type in your repsonse when I say shoot. (R, P, Sc, L, Sp)', color = 0xFFCB00)
        start.set_footer(text = 'If you have no idea what this is, use command !rpslsinfo')
        rock = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Rock', color = 0xFFCB00)
        paper = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Paper', color = 0xFFCB00)
        scissors = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Scissors', color = 0xFFCB00)
        lizard = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Lizard', color = 0xFFCB00)
        spock = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = 'Spock', color = 0xFFCB00)
        shoot = discord.Embed(title = 'Rock Paper Scissors Lizard Spock', description = '**SHOOT!**', color = 0xFFCB00)
        sending = [rock, paper, scissors, lizard, spock, shoot]

        user = {"_id": ctx.author.id}
        if (self.rpsls.count_documents(user) == 0):
            wins = 0
            ties = 0
            loses = 0
            rpsctx = {"_id": ctx.author.id, "wins": wins, "ties": ties, "loses": loses}
            self.rpsls.insert_one(rpsctx)
        else:
            for result in self.rpsls.find(user):
                wins = result["wins"]
                ties = result["ties"]
                loses = result["loses"]

        msg = await ctx.send(embed = start)
        await asyncio.sleep(4)
        for x in sending:
            await msg.edit(embed = x)
            await asyncio.sleep(0.75)
        try:
            user = await ctx.bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 15)
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out')
            return

        if user.content.lower() in userresponses:
            bot = random.choice(botresponses)
            await ctx.send(bot)
            if bot == 'Rock' and (user.content.lower() in p or user.content.lower() in sp) or bot == 'Scissors' and (user.content.lower() in r or user.content.lower() in sp) or bot == 'Paper' and (user.content.lower() in l or user.content.lower() in sc) or bot == 'Lizard' and (user.content.lower() in sc or user.content.lower() in r) or bot == 'Spock' and (user.content.lower() in l or user.content.lower() in p):
                result = 'You won!'
                wins += 1
                self.rpsls.update_one({"_id": ctx.author.id}, {"$set":{"wins":wins}})
            elif bot == 'Rock' and user.content.lower() in r or bot == 'Scissors' and user.content.lower() in sc or bot == 'Paper' and user.content.lower() in p or bot == 'Lizard' and user.content.lower() in l or bot == 'Spock' and user.content.lower() in sp:
                result = "It's a draw"
                ties += 1
                self.rpsls.update_one({"_id": ctx.author.id}, {"$set":{"ties":ties}})
            elif bot == 'Rock' and (user.content.lower() in l or user.content.lower() in sc) or bot == 'Scissors' and (user.content.lower() in p or user.content.lower() in l) or bot == 'Paper' and (user.content.lower() in r or user.content.lower() in sp) or bot == 'Lizard' and (user.content.lower() in sp or user.content.lower() in p) or bot == 'Spock' and (user.content.lower() in r or user.content.lower() in sc):
                result = 'You lost.'
                loses += 1
                self.rpsls.update_one({"_id": ctx.author.id}, {"$set":{"loses":loses}})
        else:
            await ctx.send(f'You have typed an invalid option! You lost.')
            result = 'You lost.'
            loses += 1
            self.rpsls.update_one({"_id": ctx.author.id}, {"$set":{"loses":loses}})

        record = discord.Embed(title = result, description = f'Your record in RPSLS is {wins} - {ties} - {loses}', color = 0xFFCB00)
        await ctx.send(embed = record)

#RPSLS Info
    @commands.command()
    async def rpslsinfo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = 'Info about RPSLS', color = 0xFFCB00)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/818494514867077144/853816412714958858/image0.png')
        await ctx.send(embed = embed)

#RPSStats
    @commands.command(aliases = ['rpsstats'])
    async def rockpaperscissorsstats(self, ctx, *, member: commands.MemberConverter = None):
        await ctx.message.delete()
        if member == None:
            member = ctx.author
        user = {"_id": member.id}
        if (self.rps.count_documents(user) == 0):
            wins1 = 0
            ties1 = 0
            loses1 = 0
            value1 = 'No Stats'
            winrate1 = '-'
        else:
            for result in self.rps.find(user):
                wins1 = int(result["wins"])
                ties1 = int(result["ties"])
                loses1 = int(result["loses"])
                winrate1 = round(wins1/(wins1+ties1+loses1)*100)
                value1 = f'{wins1} wins, {ties1} ties, {loses1} loses'

        if (self.rpsls.count_documents(user) == 0):
            wins2 = 0
            ties2 = 0
            loses2 = 0
            value2 = 'No Stats'
            winrate2 = '-'
        else:
            for result in self.rpsls.find(user):
                wins2 = int(result["wins"])
                ties2 = int(result["ties"])
                loses2 = int(result["loses"])
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

    @rockpaperscissorsstats.error
    async def rockpaperscissorsstats_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!rpsstats @User`', delete_after = 5.0)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Please ping a valid user', delete_after = 5.0)

#8 Ball
    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *, question):
        await ctx.message.delete()
        responses = ['It is Certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
        'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(title = '🎱 8 Ball!', description = f'Question: **__{question}__**\nBy: {ctx.author.mention}' , color = 0xFFCB00)
        embed.add_field(name = 'Response:', value = random.choice(responses))
        await ctx.send(embed = embed)

    @eightball.error
    async def eightball_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!8ball (Question)`', delete_after = 5.0)

#High 5
    @commands.command(aliases = ['high5', 'hf', 'h5'])
    async def highfive(self, ctx, *, member: commands.MemberConverter):
        await ctx.message.delete()
        if member == ctx.author:
            await ctx.send("Ok, I get that you're lonely but you can't give yourself a highfive")
        else:
            await ctx.send(f'{ctx.author.mention} has given {member.mention} a highfive. 🖐️')
            value = random.randint(1, 1000)
            if value in range(500, 505):
                await ctx.send(f'{member.mention} you also have COVID now')

    @highfive.error
    async def highfive_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use this format: `!highfive @User`', delete_after = 5.0)
        
def setup(client):
    client.add_cog(fun(client))
